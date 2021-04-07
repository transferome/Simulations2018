"""  Check haplotypes.txt files created after forqs which are fed to simreads.
  Report number of lines where snps are identical"""
import glob
import testing.transpose_data as transpose
import duplicatefinder.listduplicatecounter as duplicates
import harpsimcoverage.likereadcount as depth


def list_files():
        file_list = glob.glob('run_*/*haplotypes.txt')
        file_list.sort(key=lambda x: int(x.split('/')[0].split('-')[0].split('_')[1].lstrip('r')))
        return file_list


def snp_div(hapfile):
    same_counter = 0
    total_counter = 0
    with open(hapfile) as hf:
        for line in hf:
            if not line.startswith('3R'):
                total_counter += 1
                nucleotides = line.rstrip('\n').split(',')[1:]
                number_nucleotides = len(list(set(nucleotides)))
                if number_nucleotides > 1:
                    same_counter += 1
    return same_counter/total_counter


def count_snp_diversity():
    percentage_list = list()
    haplotype_files = list_files()
    for file in haplotype_files:
        percentage_list.append(snp_div(file))
    return percentage_list


def transp():
    duplicate_percent_list = list()
    hapfiles = list_files()
    for file in hapfiles:
        trans_data = transpose.convert(file)
        duplicate_percent_list.append(duplicates.duplicate_counter(trans_data))
    return duplicate_percent_list


def coverage():
    return depth.mean_coverage()


if __name__ == '__main__':
    test = count_snp_diversity()
    haplotype_diversity = transp()
    haplotype_depth = coverage()
