""" Given the blueprint this will make a directory """
import os
import glob
import shutil


def maindir(blueprint):
    os.mkdir('{}:{}-{}'.format(blueprint.chromosome, str(blueprint.region[0]), str(blueprint.region[1])))
    return '{}:{}-{}'.format(blueprint.chromosome, str(blueprint.region[0]), str(blueprint.region[1]))


def dat2maindir(blueprint):
    mdir = '{}:{}-{}'.format(blueprint.chromosome, str(blueprint.region[0]), str(blueprint.region[1]))
    dats = glob.glob('*.dat')
    for dat in dats:
        shutil.move(dat, mdir)

