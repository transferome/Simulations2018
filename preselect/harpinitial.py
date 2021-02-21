"""Runs harp to get frequency estimates from Generation 0 Experimental Data"""
import harpsnp.harp_freq as hfreq
import harpsnp.harp_gen0like as hlk
import harpsnp.harpclean as hclean


class Harp:
    """Runs the harp likelihood process on the different regions, using the
    blue print file to get the regions"""

    def __init__(self, sim_blueprint):
        """Takes in original window to read in the blueprint file"""
        self.chromosome = sim_blueprint.chromosome
        self.window = sim_blueprint.window
        self.region_size = sim_blueprint.region_size
        # TODO: Little unsure of subtraction of values here
        self.region = '{}:{}-{}'.format(self.chromosome,
                                        str(self.window[0] - round(self.region_size * 0.25)),
                                        str(self.window[1] + round(self.region_size * 0.25)))
        hlk.like_multi(self.chromosome, self.region)

    def freq(self, width):
        """Run the frequency command"""
        hfreq.freq_multi(self.region, width, gen='Gen0')

    def clean(self):
        """Run the cleaning class"""
        hclean.HarpClean()


if __name__ == '__main__':
    pass
