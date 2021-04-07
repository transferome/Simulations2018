import core.regionblueprint as region_blueprint
import core.harpfoundingfrequencies as estimatefounders
import core.harpgen15frequencies as estimatesamples
import core.foundinghaplotypesampling as samplefreqs
import core.processtags as tagger
import core.subregionprocess as subpar
import core.postsimulation as pst
# import graphing.combinendfreqs as grph
# import organize.movecombined as cmover
# import organize.main2results as finalmove
# import core.timetracer as tracer
import timeit


# TODO: Other experimental Fst comparisons, Up1A vs Up2A, Dwn1A vs Dwn2A, same for B's
# TODO: Verify that haplotypes are still all unique within the subregions defined during the simulation


def post(blueprint):
    pst.fst_bewtweenreplicate()
    pst.average_fst(blueprint)
    pst.mover(blueprint)


# @tracer.timer(label="Simulation Program")
def main(contig, region, recombination_simulation_number, selection_simulation_pair_number):
    """Recombination simulation number is how many times simulations will run to get the average
    recombination chunk size.
    Selection Simulation Pair number, essentially the number of simulations is this value times 2"""
    bloop = region_blueprint.preselection_recombination(contig, region, recombination_simulation_number)
    estimatefounders.harp_estimate(bloop)
    samplefreqs.starting_frequencies(selection_simulation_pair_number)
    estimatesamples.harp_final(bloop)
    # putting in 100 for the simulation of selection
    regiontags_a = tagger.make_tags(cont, selection_simulation_pair_number * 2, replicate='A')
    subpar.subregion_processes(regiontags_a, replicate='A')
    # regiontags_b = tagger.make_tags(cont, selection_simulation_pair_number * 2, replicate='B')
    # subpar.subregion_processes(regiontags_b, replicate='B')
    # post(bloop)
    # graph = grph.EndFreqs(bloop)
    # graph.combine()
    # combined_files = graph.return_files()
    # cmover.combinemove(bloop, combined_files)
    # finalmove.move2results(bloop)
    # grapher.plot_freqs(combined_files, contig, bloop)


if __name__ == '__main__':
    tic = timeit.default_timer()
    cont = '2R'
    regi = (7000000, 9000000)
    main(cont, regi, 25, 5)
    toc = timeit.default_timer()
    print(toc - tic)
