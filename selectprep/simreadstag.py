"""Tag class to handle simreads branch of code"""
import harpsnp.snp_region_min_max as minmax


class SimreadsTag:
    """Tags for Running Simreads command"""

    def __init__(self, constructor_tag):
        """Take constructor_tag to retain simulation info, and setup simreads program"""
        self.tag = constructor_tag.tag
        self.region_tag = self.tag.split('-')[0]
        self.contig = constructor_tag.contig
        self.region = constructor_tag.region
        self.region_length = constructor_tag.region_length
        self.replicate = constructor_tag.replicate
        self.sample_file = '{}-{}_rep{}.sample'.format(str(self.region[0]), str(self.region[1]), self.replicate)
        self.haplotype_file = 'run_{}/{}_haplotypes.txt'.format(self.tag, self.tag)
        self.config_file = 'run_{}/{}_simreads.config'.format(self.tag, self.tag)
        self.range_file = 'dgrp{}_rangesubset.txt'.format(constructor_tag.contig)
        self.min_max = minmax.region_min_max(self.range_file, header=False)
        self.directory = 'run_{}'.format(self.tag)
        # self.final_bam = '{}_simreads_sorted.bam'.format(self.tag)
        self.final_bam = '{}_simreads.bam'.format(self.tag)
        self.harp_region = '{}:{}-{}'.format(self.contig, str(int(self.region[0]) - 50000), str(int(self.region[1]) + 50000))
        self.harp_tag = '{}-{}_{}'.format(str(self.region[0]), str(self.region[1]), self.tag)
        self.hlk_file = '{}.hlk'.format(self.harp_tag)
        self.freq_file = '{}.freqs'.format(self.harp_tag)
        self.founding_frequency = None
        self.founding_frequency_file = '{}-{}_Gen0Rep{}.freqs'.format(str(self.region[0]), str(self.region[1]), self.replicate)
        with open(self.founding_frequency_file) as foundfile:
            for line in foundfile:
                if line.startswith('mean'):
                    self.founding_frequency = ','.join(['gen0'] + line.split(',')[3:])
                    break
        self.simulated_frequency = None
        self.final_frequency_file = '{}-{}_Rep{}_simulations.freqs'.format(str(self.region[0]), str(self.region[1]), self.replicate)
        self.fst_compare = '{}-{}_Rep{}_Fst.txt'.format(str(self.region[0]), str(self.region[1]), self.replicate)

    def get_simulated_frequencies(self):
        """This gets the mean frequencies from the frequencies simulated by harp at
        the end of the simulation and simreads.  This frequency is what will be compared to
        the founding frequency to make a statistic about haplotype frequency change given
        the simulation parameters"""
        with open(self.freq_file) as freqfile:
            for line in freqfile:
                if line.startswith('mean'):
                    self.simulated_frequency = ','.join([self.tag] + line.split(',')[3:])
                    break


if __name__ == '__main__':
    pass
