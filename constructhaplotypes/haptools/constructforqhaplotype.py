"""Functions for constructing haplotypes for simreads from forqs, using
the population file list, the snp position list and haplotype dictionary"""
from . import indexgetter as idxgetter
import numpy as np


class ForqsHaplotype:
    """Forqs Haplotype Object
    Example [(0, 91), (1235052, 105), (1251805, 105)]
    or  [(0, 91)]
    """

    def __init__(self, forq_haplotype):
        """Forqs Haplotype Instance Creation"""
        self.info = forq_haplotype

        # tag object depending on it's structure
        self.length = len(self.info)
        self.founders = [haplotype_id for position, haplotype_id in self.info]
        self.founders_set = list(set(self.founders))
        self.founder_number = len(self.founders_set)
        self.positions = [position for position, haplotype_id in self.info]
        self.struct = 'normal'
        if self.length == 1:
            self.struct = 'single'
        if self.length != self.founder_number:
            self.struct = 'contain duplicate'
        if self.length == 2 and self.founder_number == 1:
            self.struct = 'single recombined'
        self.position_map_offset = None
        self.temp_map = None
        self.map = list()

    def make_haplotype_map(self, snp_position_list):
        """Create the haplotype guide for assembling the recombined forqs haplotype outputs"""
        position_indexes = [idx for idx, position in snp_position_list]
        position_values = [position for idx, position in snp_position_list]
        min_index = min(position_indexes)
        max_index = max(position_indexes)
        # within population haplotype files these matter
        if self.struct == 'single' or self.struct == 'single recombined':
            self.map.append([self.founders_set[0], min_index, max_index])
        if self.struct == 'normal' or self.struct == 'contain duplicate':
            if self.positions[1] < min(position_values):
                self.founders.pop(0)
                self.positions.pop(1)
            try:
                if self.positions[2] < min(position_values):
                    print("Two recombination points before the first SNP occurs")
                    quit()
            except IndexError:
                pass
            self.position_map_offset = self.positions[1:] + [max(position_values)]
            self.temp_map = list(zip(self.positions, self.position_map_offset))
            for hap in self.temp_map:
                min_id, max_id = idxgetter.index_getter(hap[0], hap[1], snp_position_list)
                self.map.append([min_id, max_id])
            for i, hap_map in enumerate(self.map):
                if i < len(self.map) - 1:
                    current_end = hap_map[1]
                    next_start = self.map[i + 1][0]
                    # print(current_end, next_start)
                    if current_end == next_start:
                        self.map[i + 1][0] = int(next_start) + 1
            for line_id, hap_map in zip(self.founders, self.map):
                hap_map.insert(0, line_id)


def construct_individual(forq_haplotype_object, hap_dict):
    """Given the output from parse_individual, and the haplotype_dictionary, this creates
    an individuals haplotype"""
    if forq_haplotype_object.struct == 'single' or forq_haplotype_object.struct == 'single recombined':
        haplotype = hap_dict[str(forq_haplotype_object.founders_set[0])]
        sequence_chunk = haplotype[forq_haplotype_object.map[0][1]:forq_haplotype_object.map[0][2] + 1]
        return sequence_chunk
    if forq_haplotype_object.struct == 'normal' or forq_haplotype_object.struct == 'contain duplicate':
        sequence_list = list()
        for sub_map in forq_haplotype_object.map:
            haplotype = hap_dict[str(sub_map[0])]
            sequence_list.append(haplotype[sub_map[1]:sub_map[2] + 1])
        return ''.join(sequence_list)


def process_population(poplist, snp_position_list, hap_dict):
    """Given the population list from a read in popfile, this constructs haplotypes for all individuals"""
    haplist = list()
    templist = list()
    outlist = list()
    for line in poplist:
        individual = ForqsHaplotype(line)
        individual.make_haplotype_map(snp_position_list)
        haplist.append(construct_individual(individual, hap_dict))
    for hap in haplist:
        new_hap = list(hap)
        templist.append(new_hap)
    hap_array = np.array(templist)
    hap_trans = hap_array.transpose()
    new_hap_list = hap_trans.tolist()
    for lst in new_hap_list:
        new_line = ','.join(lst)
        outlist.append(new_line)
    return outlist


if __name__ == '__main__':
    pass




