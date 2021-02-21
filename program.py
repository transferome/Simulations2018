import core.regionblueprint as region_blueprint
import core.harpfoundingfrequencies as estimatefounders
import core.harpgen15frequencies as estimatesamples
import core.foundinghaplotypesampling as samplefreqs
import core.processtags as tagger
import core.simreads as simreads
import core.harpsimulatedfrequencies as simharp
import core.postsimulation as pst
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
        simharp.fst_whithinreplicate(stags)


def post(blueprint):
    pst.fst_bewtweenreplicate()
    pst.average_fst(blueprint)
    pst.mover(blueprint)


if __name__ == '__main__':
    cont = '3R'
    regi = (7000000, 9000000)
    # this is number of simulations to determine recombination intervals
    sim_num = 10
    bloop = region_blueprint.preselection_recombination(cont, regi, sim_num)
    estimatefounders.harp_estimate(bloop)
    samplefreqs.starting_frequencies(2)
    estimatesamples.harp_final(bloop)
    # putting in 100 for the simulation of selection
    regiontagsA = tagger.make_tags(cont, 4, replicate='A')
    subregion_processes(regiontagsA, replicate='A')
    regiontagsB = tagger.make_tags(cont, 4, replicate='B')
    subregion_processes(regiontagsB, replicate='B')
    post(bloop)
