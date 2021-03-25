"""  Class Object to Run Harp Likelihood process on the gen 15 data  """
import subprocess
from multiprocessing import Pool
from functools import partial
from . import resources_dir
import psutil
import os


sample_dict = {'S1_sorted_proper_realigned.bam': 'Gen15Up1A', 'S2_sorted_proper_realigned.bam': 'Gen15Up2A',
               'S3_sorted_proper_realigned.bam': 'Gen15Dwn1A', 'S4_sorted_proper_realigned.bam': 'Gen15Dwn2A',
               'S5_sorted_proper_realigned.bam': 'Gen15CtrlA',
               'S6_sorted_proper_realigned.bam': 'Gen15Up1B', 'S7_sorted_proper_realigned.bam': 'Gen15Up2B',
               'S8_sorted_proper_realigned.bam': 'Gen15Dwn1B', 'S9_sorted_proper_realigned.bam': 'Gen15Dwn2B',
               'S10_sorted_proper_realigned.bam': 'Gen15CtrlB'}

snp_files = {'2L': '{}/2L_snp_good.txt'.format(resources_dir),
             '2R': '{}/2R_snp_good.txt'.format(resources_dir),
             '3L': '{}/3L_snp_good.txt'.format(resources_dir),
             '3R': '{}/3R_snp_good.txt'.format(resources_dir)}


def limit_cpu():
    """Called at Every Process in Pool and sets niceness"""
    p = psutil.Process(os.getpid())
    p.nice(3)


def like_process(chromosome, region, gen15_bam):
    """Execute harp like command and process on particular
    Generation 15 bam file"""
    ref_file = '{}/dmel-majchr-norm-r6.24.fasta'.format(resources_dir)
    # use rangesubset to get min max SNP positions
    harp_like_command = ['harp', 'like', '--bam', '{}/{}'.format(resources_dir, gen15_bam), '--region', region,
                         '--refseq', ref_file, '--snps', snp_files[chromosome], '--stem',
                         '{}_{}'.format(region, sample_dict[gen15_bam])]
    # print(harp_like_command)
    subprocess.call(harp_like_command, shell=False)


def like_multi(chromosome, region):
    bams = list(sample_dict.keys())
    pool = Pool(21, limit_cpu)
    likef = partial(like_process, chromosome, region)
    pool.map(likef, bams)


if __name__ == '__main__':
    pass
