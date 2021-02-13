"""Functions to handle simreads aspect of a """
import simreads.simreadsparallel as simreadsparallel
import simreads.samtoolsviewparallel as view
import simreads.samtoolssortparallel as sorter
import simreads.samtoolsindexparallel as sindex
import simreads.cleansimreads as simcleaner


def simreads_parallel(simreads_tags):
    """Given a set of constructor_tags, runs simreads in parallel
    All constructor tags given when function called should have same region tag
    function returns a region tag from one of the constructor tags
    which is then passed to the simreads_process function"""
    simreadsparallel.simreads_multi(simreads_tags)
    return simreads_tags[0].region_tag


def simreads_process(simread_tag_region_tag):
    view.samtools_view_multi(simread_tag_region_tag)
    sorter.samtools_sort_multi(simread_tag_region_tag)
    sindex.samtools_index_multi(simread_tag_region_tag)
    simcleaner.removesams(simread_tag_region_tag)
    simcleaner.removebams(simread_tag_region_tag)
    simcleaner.movefreqs(simread_tag_region_tag)


def simreads_run(simreads_tags):
    sim_reg_tag = simreads_parallel(simreads_tags)
    simreads_process(sim_reg_tag)


if __name__ == '__main__':
    pass
