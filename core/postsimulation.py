"""  Some processes to do once all the simulations have completed  """
import fst.fstbetweenreplicate as fstbetweenf
import fst.avgfst as avg
import glob
import shutil
import subprocess
import organize.directorymaker as mydir


def fst_bewtweenreplicate():
    fstbetweenf.fst_between()


def average_fst(blueprint):
    avgblp = avg.AvgFst(blueprint)
    avgblp.files_regions()
    avgblp.gather_data()
    avgblp.write_sum()


def folder_move(source, destination):
    subprocess.call(['mv', source, destination], shell=False)


def mover(blueprint):
    csvs = glob.glob('*.csv')
    freqs = glob.glob('*.freqs')
    txts = glob.glob('*.txt')
    dats = glob.glob('*.dat')
    main_direct = mydir.main_dir(blueprint)
    junk_direct = mydir.junk_dir(blueprint)
    fst_direct = mydir.fst_dir(blueprint)
    endfreq_direct = mydir.endfreq_dir(blueprint)
    for csv in csvs:
        shutil.move(csv, junk_direct)
    for freq in freqs:
        if 'combined' not in freq:
            shutil.move(freq, junk_direct)
    for txt in txts:
        shutil.move(txt, junk_direct)
    for dat in dats:
        shutil.move(dat, fst_direct)
    folder_move(junk_direct, main_direct)
    folder_move(fst_direct, main_direct)
    folder_move(endfreq_direct, main_direct)


if __name__ == '__main__':
    pass
