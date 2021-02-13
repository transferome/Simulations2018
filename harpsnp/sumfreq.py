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


def sumfreq(chromosome):
    freqs = glob.glob('*.freqs')
    freqs = [s for s in freqs if chromosome not in s]
    for freq in freqs:
        df = read_freq(chromosome, freq)
        mean_vals = df.mean(axis=0).tolist()
        mean = ["{:.5f}".format(float(num)) for num in mean_vals]
        mean.insert(0, 'mean')
        var_vals = df.var(axis=0).tolist()
        var = ["{:.8f}".format(float(num)) for num in var_vals]
        var.insert(0, 'var')
        df.loc[len(df.index)] = mean
        df.loc[len(df.index)] = var
        df.to_csv(path_or_buf=freq, sep=',', header=True, index=False)


if __name__ == '__main__':
    pass
