"""Sum frequencies and add header to a subset freq file"""
import glob
import pandas as pd
from . import resources_dir


def get_header(chromosome):
    """get the header from the snp text file given the chromosome"""
    with open('{}/{}_snp_good.txt'.format(resources_dir, chromosome)) as infile:
        header = infile.readline().rstrip('\n')
        keep = header.split(',')[2:]
        new_header = [chromosome, 'start', 'end'] + keep
        return new_header


def read_freq(chromosome, freqfile):
    """read the freq file and give it a header"""
    headin = get_header(chromosome)
    file = pd.read_csv(freqfile, sep=',', names=headin)
    return file



class SumFreq:

    def __init__(self, chromosome):
        self.chromosome = chromosome
        freqs = glob.glob('*.freqs')
        self.freqs = [s for s in freqs if self.chromosome not in s]

    def sumf(self):
        for freq in self.freqs:
            # print(freq)
            df = read_freq(self.chromosome, freq)
            mean_vals = df.mean(axis=0).tolist()
            mean = ["{:.5f}".format(float(num)) for num in mean_vals]
            mean.insert(0, 'mean')
            var_vals = df.var(axis=0).tolist()
            var = ["{:.8f}".format(float(num)) for num in var_vals]
            var.insert(0, 'var')
            df.loc[len(df.index)] = mean
            df.loc[len(df.index)] = var
            df.to_csv(path_or_buf=freq, sep=',', header=True, index=False)


class SumFreqEnd(SumFreq):
    """Sum up files resulting from estimating Generation 15 haplotype frequencies"""

    def __init__(self, chromosome):
        super(SumFreqEnd, self).__init__(chromosome)
        self.chromosome = chromosome
        freqs = glob.glob('*Gen15*.freqs')
        self.freqs = [s for s in freqs if self.chromosome not in s]


if __name__ == '__main__':
    pass
