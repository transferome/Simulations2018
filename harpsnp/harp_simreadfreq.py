"""Estimate haplotype frequencies in 100kb windows with
a 10kb step"""
import subprocess
from multiprocessing import Pool


def freq_process(simreads_tag):
    """Executes harp freq command"""
    harp_freq_command = ['harp', 'freq', '--hlk', simreads_tag.hlk_file,
                         '--region', simreads_tag.harp_region, '--window_step',
                         '10000', '--window_width', '100000']
    subprocess.check_call(harp_freq_command, shell=False)


def freq_multi(simreads_tags):
    """runs harp freq in parallel using the simreads_tags"""
    pool = Pool(21)
    pool.map(freq_process, simreads_tags)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
