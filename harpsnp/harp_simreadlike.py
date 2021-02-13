"""Harp likelihood process on the sorted bam files
created by the simreads package"""
import subprocess
from multiprocessing import Pool
from . import resources_dir


def like(simreads_tag):
    """Makes the command and calls it using a simreads tag"""
    ref_file = '{}/dmel-majchr-norm-r6.24.fasta'.format(resources_dir)
    snp_txt = '{}/{}_snp_good.txt'.format(resources_dir, simreads_tag.contig)
    harp_like_command = ['harp', 'like', '-I', '--bam', simreads_tag.final_bam,
                         '--region', simreads_tag.harp_region,
                         '--refseq', ref_file, '--snps', snp_txt,
                         '--stem', simreads_tag.harp_tag]
    subprocess.call(harp_like_command, shell=False)


def like_multi(simreads_tags):
    """Runs harp like function in parallel"""
    pool = Pool(21)
    pool.map(like, simreads_tags)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pass
