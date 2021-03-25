"""  Runs harp and calculates frequencies in the window on all of the sample files
  at gen 15 as well.  In order to get average frequencies for comparison of Fst within that window"""
import preselect.harpfinal as harpf
import preselect.handlefreqs as sub
import harpsnp.sumfreq as summer
import fst.fstendfreqs as fst
# import core.timetracer as timer


# @timer.timer(label="HarpEnd")
def harp_final(blueprint):
    hpf = harpf.HarpEnd(blueprint)
    hpf.like()
    hpf.freq(blueprint.region_size)
    enclean = harpf.clean()
    subsetter = sub.SplitEnds(blueprint.file)
    subsetter.split_end()
    endfreq = summer.SumFreqEnd(blueprint.chromosome)
    endfreq.sumf()
    subsetter.gather_end()
    fst.endfst()
    enclean.move_freq(blueprint)


if __name__ == '__main__':
    pass
