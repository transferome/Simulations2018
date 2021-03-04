"""  Module to make graphs of the Fst values  """
import os
import glob
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import rcParams
from numpy import linspace
# on linux
rcParams['font.family'] = "DejaVu Sans Mono"


plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "white",
    "axes.facecolor": "black",
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "black",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "font.monospace": "monospace",
    "savefig.edgecolor": "black",
    "figure.max_open_warning": 0})


class FstClass:

    def __init__(self, directory, chromosome, treatment1, treatment2):
        """Gets the list of positions from the file"""
        self.directory = directory
        os.chdir(self.directory)
        self.chromosome = chromosome
        self.expdat = 'Exp_{}_{}_Fst.dat'.format(treatment1, treatment2)
        self.simdat = glob.glob('*_Simulation_Fst.dat')[0]
        self.region = None
        # self.file2 = filename2
        with open(self.expdat) as f:
            self.data = [line.rstrip('\n') for line in f]
        self.expos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data]
        self.expos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data]
        self.ex_startpos = self.expos1[0]
        self.ex_endpos = self.expos2[-1]
        self.ex_region = '{}:{}-{}'.format(self.chromosome, str(self.ex_startpos), str(self.ex_endpos))
        with open(self.simdat) as f2:
            self.data2 = [line.rstrip('\n') for line in f2 if not line.startswith('region')]
        self.simpos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data2]
        self.simpos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data2]
        self.sim_startpos = self.simpos1[0]
        self.sim_endpos = self.simpos2[-1]
        self.sim_region = '{}:{}-{}'.format(self.chromosome, str(self.sim_startpos), str(self.sim_endpos))
        if self.ex_region != self.sim_region:
            print("Problem")
            quit()
        else:
            self.region = self.ex_region
        self.ex_dict = {idx: None for idx, col in enumerate(self.data[0].split(','))}
        del self.ex_dict[0]
        for key in self.ex_dict.keys():
            fst_list = list()
            for line in self.data:
                fst_list.append(round(float(line.split(',')[key]), 4))
            self.ex_dict[key] = fst_list
        self.sim_dict = {idx: None for idx, col in enumerate(self.data2[0].split(','))}
        del self.sim_dict[0]
        for key in self.sim_dict.keys():
            sim_fst_list = list()
            for line in self.data2:
                sim_fst_list.append(round(float(line.split(',')[key]), 4))
            self.sim_dict[key] = sim_fst_list

        self.range_list = list()
        for a, b in zip(self.expos1, self.expos2):
            # subtract 1, so that range
            self.range_list.append(range(a, b))
        self.outputfile = '{}_vs_{}_Fst.png'.format(treatment1, treatment2)
        self.title = '{} & {}       {}'.format(treatment1, treatment2, self.region)
        self.x_label = 'Genomic Coordinate'
        # TODO: need to add variance to Fst when calculating so you can make error bars in graph (possibly)
        self.y_label = 'Fst (mean value for simulation data)'
        self.fig = None
        self.ax = None
        self.ymax = None
        self.colormap1 = ['darkorchid', 'indigo', 'royalblue']
        self.colormap2 = ['pink']

    def find_ymax(self):
        max_val = 0
        for key in self.ex_dict.keys():
            freqs_check = self.ex_dict[key]
            new_max = round(max(freqs_check), 2)
            if new_max > max_val:
                max_val = new_max
        for key in self.sim_dict.keys():
            chekker = self.sim_dict[key]
            new_max2 = round(max(chekker), 2)
            if new_max2 > max_val:
                max_val = new_max2
        self.ymax = round(max_val, 2)
        # print(str(self.ymax))

    def plot(self):
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1, figsize=(20, 10))
        self.ax.set_ylim([0, self.ymax + 0.05])
        xlim = len(range(1, 1000)) * len(self.range_list)
        self.ax.set_xlim([1, xlim])
        self.ax.set_title(self.title, fontsize=20)
        for key, color_iterator in zip(self.ex_dict.keys(), self.colormap2):
            y_data = list()
            for rng, freq in zip(self.range_list, self.ex_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, linewidth=5.0)
        for key, color_iterator in zip(self.sim_dict.keys(), self.colormap1):
            y_data = list()
            for rng, freq in zip(self.range_list, self.sim_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, linewidth=5.0)
        # self.ax.set_xticks([idx for idx, s in enumerate(self.positions)])
        xticks = list(range(1, xlim, 1000))
        xticklables = ["{:,}".format(x) for x in self.expos1]
        # yrange = range(0, self.ymax + 0.05, 0)
        # yticks = [0.2, 0.4, 0.6, 0.8]
        # yticklabels = ['0.2', '0.4', '0.6', '0.8']
        self.ax.set_xticks(xticks[0::2])
        self.ax.set_xticklabels(xticklables[0::2])
        plt.setp(self.ax.get_xticklabels(), fontsize=15)
        plt.setp(self.ax.get_yticklabels(), fontsize=15)
        self.ax.set_ylabel('Haplotype Fequency', fontsize=16)
        self.ax.set_xlabel(self.x_label, fontsize=16)

test = FstClass("/home/solid-snake/pyreseq/SimulationsPrior", '2R', 'Up1A', 'Dwn1A')
test.find_ymax()
test.plot()
test.fig.show()