"""Data Class For Harp .freq files, Can also make some plots from data"""
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
from matplotlib import rcParams
from matplotlib import cm
from numpy import linspace
rcParams['font.family'] = "serif"


class FreqPlot:
    """Handles Harp Concatenated Harp Files.  Example 2L_harp_pool.txt"""
    def __init__(self, filepath, contig):
        self.file = filepath
        self.chromosome = contig
        self.header = None
        self.old_header = None
        # turns the regions headers into the start of the region instead of the start - end
        self.regions_x = None
        self.dgrp_lines = None
        self.harp_sample = None
        self.fig = None
        self.ax = None
        file_data = [line.strip('\n') for line in open(self.file)]
        self.data = file_data[1:]
        self.old_header = file_data[0]
        header_temp = self.old_header.split('\t')
        header_regions = header_temp[2:]
        # x data the first number in the regions range
        self.regions_x = [int(s.split('-')[0]) for s in header_regions]

        new_header = list(range(1, len(header_regions) + 1))
        self.header = new_header
        self.harp_sample = {line.split('\t')[0]: [float(x) for x in line.split('\t')[2:]] for line in self.data}
        self.dgrp_lines = list(self.harp_sample.keys())

    def return_plot(self, sample_info, xinch, yinch, color_map):
        """Returns a Figure"""
        y_dict = self.harp_sample
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1, figsize=(xinch, yinch))
        self.ax.set_title(f'{sample_info}', fontsize=18)
        x_data = self.regions_x
        for key, color_iterator in zip(y_dict.keys(), color_map):
            y_data = y_dict[key]
            self.ax.plot(x_data, y_data, color=color_iterator)
        self.ax.get_xaxis().get_major_formatter().set_scientific(False)
        self.ax.get_xaxis().set_major_formatter(tick.FuncFormatter(lambda x, p: format(int(x), ',')))
        plt.setp(self.ax.get_xticklabels(), fontsize=14)
        plt.setp(self.ax.get_yticklabels(), fontsize=14)
        self.ax.set_ylabel('Fequency', fontsize=18)
        self.ax.set_xlabel(self.chromosome, fontsize=18)


if __name__ == '__main':
    contig = '3R'
    step = '100k'
    samples = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S21', 'S22']
    for sample in samples:
        dat = FreqPlot('{}_{}step/{}_{}.txt'.format(contig, step, sample, contig), contig)
        len(dat.dgrp_lines)
        cm_subsection = linspace(0, 1, len(dat.dgrp_lines))
        colors = [cm.tab10(x) for x in cm_subsection]
        dat.return_plot('{}_{}_{}'.format(sample, contig, step), 20, 10, colors)
        # dat.fig.show()
        dat.fig.savefig('{}_{}step/{}_{}_{}.png'.format(contig, step, sample, contig, step))
        plt.close(dat.fig)

