"""Estimates frequencies and organizes them for the simulated bam files created from
simulations of the artificial selection at Gen0 to Gen 15"""
import harpsnp.harp_simreadfreq as harpfreq
import harpsnp.harp_simreadlike as harplike
import harpsnp.simread_sumfreq as simfreq


def simreads_harp(simreads_tags):
    """Runs simreads on the simulated frequencies, creates mean frequencies in fashion
    similar to founding frequencies, multiple windows that need to have 75% overlap with the
    region the mean frequency is for"""
    harplike.like_multi(simreads_tags)
    harpfreq.freq_multi(simreads_tags)
    simfreq.sumtag_freqs(simreads_tags)


if __name__ == '__main__':
    pass
