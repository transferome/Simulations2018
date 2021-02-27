"""  Moves combined files into the dat2graph subdirectory  """
import shutil
import organize.directorymaker as dirmkdir
import subprocess


def combinemove(bloop, combined_files):
    graphdir = dirmkdir.graph_dir(bloop)
    for file in combined_files:
        shutil.move(file, graphdir)
    maindir = dirmkdir.main_dir(bloop)
    subprocess.call(['mv', graphdir, '{}/'.format(maindir)], shell=False)


if __name__ == '__main__':
    pass
