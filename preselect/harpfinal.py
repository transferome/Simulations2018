"""  Class object to run harp on a region and window size within the experimental
bam files at Generation 15"""
import harpsnp.harp_gen15like as hlk_end
import harpsnp.harp_freq as hfreq
import harpsnp.harpclean as hclean_end


def clean():
    """Cleans up the files"""
    return hclean_end.HarpEndClean()


class HarpEnd:
    """Runs harp on the Generation 15 files and cleans up"""

    def __init__(self, sim_bluprint):
        """Takes in the original window to read the blueprint and estimate
        frequencies along that window"""
        self.contig = sim_bluprint.chromosome
        self.window = sim_bluprint.window
        self.region_size = sim_bluprint.region_size
        self.region = '{}:{}-{}'.format(self.contig,
                                        str(self.window[0] - round(self.region_size * 0.25)),
                                        str(self.window[1] + round(self.region_size * 0.25)))

    def like(self):
        hlk_end.like_multi(self.contig, self.region)

    def freq(self, width):
        hfreq.freq_multi(self.region, width, gen='Gen15')


if __name__ == '__main__':
    pass
