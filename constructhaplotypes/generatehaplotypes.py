"""Generate haplotypes from the forqs population files"""
import constructhaplotypes.haptools.haplotypedict as hdict
# import constructhaplotypes.haptools.positionindex as posidx
import constructhaplotypes.haptools.readpopfile as popread
import constructhaplotypes.haptools.forqshaplotype as constructor
import constructhaplotypes.haptools.writesnptable as writer


def generate(constructor_tag):
    """Makes haplotypes"""
    ref_file = 'dgrp{}_subset.txt'.format(constructor_tag.contig)
    # pos_id_list = posidx.position_index(constructor_tag)
    hap_dict = hdict.haplodict(constructor_tag)
    pop_file = popread.readpop(constructor_tag.population_file)
    output_haplotypes = constructor.process_population(pop_file, hap_dict, constructor_tag.haplotype_id_dict)
    # print(output_haplotypes)
    writer.write_snp_table(ref_file, output_haplotypes, constructor_tag)


if __name__ == '__main__':
    pass
