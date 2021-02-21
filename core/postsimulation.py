"""  Some processes to do once all the simulations have completed  """
import fst.fstbetweenreplicate as fstbetweenf
import fst.avgfst as avg
import glob
import shutil
import os


def fst_bewtweenreplicate():
    fstbetweenf.fst_between()


def average_fst(blueprint):
    avgblp = avg.AvgFst(blueprint)
    avgblp.files_regions()
    avgblp.gather_data()
    avgblp.write_sum()


def mover(blueprint):
    csvs = glob.glob('*.csv')
    freqs = glob.glob('*.freqs')
    txts = glob.glob('*.txt')
    direct = '{}_{}-{}'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    os.mkdir(direct)
    for csv in csvs:
        shutil.move(csv, direct)
    for freq in freqs:
        shutil.move(freq, direct)
    for txt in txts:
        shutil.move(txt, direct)


if __name__ == '__main__':
    pass
