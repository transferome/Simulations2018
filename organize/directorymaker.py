""" Given the blueprint this will make a directory """
import os


def creator(pathname):
    if not os.path.exists(pathname):
        os.mkdir(pathname)
        return pathname
    else:
        return pathname


def main_dir(blueprint):
    path = '{}_{}-{}'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


def junk_dir(blueprint):
    path = '{}_{}-{}_junk'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


def endfreq_dir(blueprint):
    path = '{}_{}-{}_end_freqs'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


def fst_dir(blueprint):
    path = '{}_{}-{}_Fst'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


def graph_dir(blueprint):
    path = '{}_{}-{}_data2graph'.format(blueprint.chromosome, str(blueprint.window[0]), str(blueprint.window[1]))
    return creator(path)


if __name__ == '__main__':
    pass
