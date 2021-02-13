"""Common Functions Used In Different Simulation Module scripts"""
import os
import glob


def list_bams(chromosome):
    """Lists all sorted bam files"""
    return glob.glob('*{}*.bam'.format(chromosome))


def list_hlk(chromosome):
    """Lists all hlk files in folder"""
    return glob.glob('{}:*.hlk'.format(chromosome))


def remove_hlk(chr_arm):
    """Removes the hlk files, they are large"""
    hlks = list_hlk(chr_arm)
    for hlk in hlks:
        os.remove(hlk)


if __name__ == '__main__':
    pass
