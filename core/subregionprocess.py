"""  Seeing if subregion can be run in parallel  """
import core.processtags as tagger
import core.simreads as simreads
import core.harpsimulatedfrequencies as simharp
import harpsnp.harpclean as simclean


def subregion_processes(region_tags, replicate='A'):
    """processes the individual subregions created by the blueprint"""
    for region_tag in region_tags:
        ftag = tagger.makeforqs_run(region_tag)
        ctags = tagger.make_constructor_tags(ftag, replicate)
        tagger.make_haplotypes(ctags)
        stags = tagger.make_simreads_tags(ctags)
        tagger.write_simread_configs(stags)
        simreads.simreads_run(stags)
        simharp.simreads_harp(stags)
        simharp.gen0combine(replicate)
        simclean.HarpSimClean()
        tagger.add_simfrequency_attribute(stags)
        tagger.write_frequency_comparison_file(stags)
        tagger.clean_region(stags)
        simharp.fst_whithinreplicate(stags)


if __name__ == '__main__':
    pass
