""" Given the blueprint this will make a directory """
import os


def creator(pathname):
    if not os.path.exists(pathname):
        os.mkdir(pathname)
        return pathname
    else:
        return pathname


def main_dir(blueprint):
    path = '{}:{}-{}'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


def junk_dir(blueprint):
    path = '{}:{}-{}_junk'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


def endfreq_dir(blueprint):
    path = '{}:{}-{}_end_freqs'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


def fst_dir(blueprint):
    path = '{}:{}-{}_Fst'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


if __name__ == '__main__':
    pass
