"""Multiprocessing of harp like command"""
import subprocess
from multiprocessing import Pool
from functools import partial
from . import resources_dir
import psutil
import os


def limit_cpu():
    """Called At Every Process Started in a multiprcoess pool"""
    p = psutil.Process(os.getpid())
    p.nice(3)


def like_process(chromosome, region, bam):
    """Execute harp like command and process"""
    # ref file is always the same
    if 'S21' in bam:
        stem = '{}_Gen0RepAMaster'.format(region)
    else:
        stem = '{}_Gen0RepBMaster'.format(region)
    ref_file = '{}/dmel-majchr-norm-r6.24.fasta'.format(resources_dir)
    # snp_text will be based off chromosome arm
    snp_text = '{}/{}_snp_good.txt'.format(resources_dir, chromosome)
    # use rangesubset to get min max SNP positions
    harp_like_command = ['harp', 'like', '--bam', bam, '--region', region, '--refseq', ref_file, '--snps',
                         snp_text, '--stem', stem]
    subprocess.call(harp_like_command, shell=False)


def like_multi(chromosome, region):
    """Runs harp like function in parallel"""
    bam_file_list = ['{}/S21_sorted_proper_realigned.bam'.format(resources_dir),
                     '{}/S22_sorted_proper_realigned.bam'.format(resources_dir)]
    pool = Pool(21, limit_cpu)
    adjusted_func = partial(like_process, chromosome, region)
    pool.map(adjusted_func, bam_file_list)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
