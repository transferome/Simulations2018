import core.regionblueprint as region_blueprint
import core.harpfoundingfrequencies as estimatefounders
import core.harpgen15frequencies as estimatesamples
import core.foundinghaplotypesampling as samplefreqs
import core.processtags as tagger
import core.subregionprocess as subpar
import core.postsimulation as pst
import core.timetracer as tracer


def post(blueprint):
    pst.fst_bewtweenreplicate()
    pst.average_fst(blueprint)
    pst.mover(blueprint)


@tracer.timer(label="Simulation Program")
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
    regiontags_b = tagger.make_tags(cont, selection_simulation_pair_number * 2, replicate='B')
    subpar.subregion_processes(regiontags_b, replicate='B')
    post(bloop)


if __name__ == '__main__':
    cont = '2R'
    regi = (7000000, 9000000)
    main(cont, regi, 20, 20)
    # bloop = region_blueprint.preselection_recombination(cont, regi, sim_num)
    # estimatefounders.harp_estimate(bloop)
    # samplefreqs.starting_frequencies(20)
    # estimatesamples.harp_final(bloop)
    # # putting in 100 for the simulation of selection
    # regiontagsA = tagger.make_tags(cont, 40, replicate='A')
    # subpar.subregion_processes(regiontagsA, replicate='A')
    # regiontagsB = tagger.make_tags(cont, 40, replicate='B')
    # subpar.subregion_processes(regiontagsB, replicate='B')
    # post(bloop)
