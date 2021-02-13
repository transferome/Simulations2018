"""Multiprocessing of harp freq command"""
import subprocess
from multiprocessing import Pool
from functools import partial
import glob


def make_step(width):
    """Creates a step that is 10% of the window size"""
    return str(round(width * 0.10))


def freq_process(region, width, hlk_file):
    """Executes harps freq command"""
    harp_freq_command = ['harp', 'freq', '--hlk', hlk_file, '--region', region, '--window_step',
                         make_step(width), '--window_width', str(width)]
    subprocess.check_call(harp_freq_command, shell=False)


def freq_multi(region, width):
    """runs harp freq in parallel multiprocess"""
    hlks = glob.glob('*_Gen0*.hlk')
    pool = Pool(21)
    adjusted_func = partial(freq_process, region, width)
    pool.map(adjusted_func, hlks)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
    # freq_multi(args.chr, args.step, args.width, freq_process)
    # renamer(args.chr, args.step, args.width)
    # mover(args.chr, args.width)
