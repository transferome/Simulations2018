import core.regionblueprint as region_blueprint
import core.harpfoundingfrequencies as estimatefounders
import core.foundinghaplotypesampling as samplefreqs
import core.processtags as tagger
import core.simreads as simreads
import core.harpsimulatedfrequencies as simharp
import harpsnp.harpclean as simclean


def subregion_processes(region_tags, replicate='A'):
    """processes the individual subregions created by the blueprint"""
    for tag in region_tags:
        ftag = tagger.makeforqs_run(tag)
        ctags = tagger.make_constructor_tags(ftag, replicate)
        tagger.make_haplotypes(ctags)
        stags = tagger.make_simreads_tags(ctags)
        tagger.write_simread_configs(stags)
        simreads.simreads_run(stags)
        simharp.simreads_harp(stags)
        simclean.HarpSimClean()
        tagger.add_simfrequency_attribute(stags)
        tagger.write_frequency_comparison_file(stags)
        tagger.clean_region(stags)


if __name__ == '__main__':
    cont = '2R'
    regi = (8000000, 10000000)
    sim_num = 20
    bloop = region_blueprint.preselection_recombination(cont, regi, sim_num)
    estimatefounders.harp_estimate(bloop)
    samplefreqs.starting_frequencies()
    regiontagsA = tagger.make_tags(cont, sim_num, replicate='A')
    subregion_processes(regiontagsA, replicate='A')
    regiontagsB = tagger.make_tags(cont, sim_num, replicate='B')
    subregion_processes(regiontagsB, replicate='B')
