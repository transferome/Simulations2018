import core.regionblueprint as region_blueprint
import core.harpfoundingfrequencies as estimatefounders
import core.harpgen15frequencies as estimatesamples
import core.foundinghaplotypesampling as samplefreqs
import core.postsimulation as pst


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


if __name__ == '__main__':
    cont = '2R'
    regi = (7000000, 9000000)
    main(cont, regi, 20, 50)