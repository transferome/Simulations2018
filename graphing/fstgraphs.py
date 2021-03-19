"""  Module to make graphs of the Fst values  """
import os
import glob
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.lines import Line2D
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

    def __init__(self, directory, chromosome):
        """Gets the list of positions from the file"""
        self.directory = directory
        os.chdir(self.directory)
        self.chromosome = chromosome
        self.expdat1A = 'Exp_Up1A_Dwn1A_Fst.dat'
        self.expdat2A = 'Exp_Up2A_Dwn2A_Fst.dat'
        self.expdat1B = 'Exp_Up1B_Dwn1B_Fst.dat'
        self.expdat2B = 'Exp_Up2B_Dwn2B_Fst.dat'
        self.cdat = glob.glob('*_CtrlA_CtrlB_Fst.dat')[0]
        self.simdat = glob.glob('*_Simulation_Fst.dat')[0]
        self.region = None
        with open(self.expdat1A) as f:
            self.data1A = [line.rstrip('\n') for line in f]
        self.A1pos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data1A]
        self.A1pos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data1A]
        self.A1_startpos = self.A1pos1[0]
        self.A1_endpos = self.A1pos2[-1]
        self.A1_region = '{}:{}-{}'.format(self.chromosome, str(self.A1_startpos), str(self.A1_endpos))
        with open(self.expdat2A) as f:
            self.data2A = [line.rstrip('\n') for line in f]
        self.A2pos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data2A]
        self.A2pos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data2A]
        self.A2_startpos = self.A2pos1[0]
        self.A2_endpos = self.A2pos2[-1]
        self.A2_region = '{}:{}-{}'.format(self.chromosome, str(self.A2_startpos), str(self.A2_endpos))
        with open(self.expdat1B) as f:
            self.data1B = [line.rstrip('\n') for line in f]
        self.B1pos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data1B]
        self.B1pos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data1B]
        self.B1_startpos = self.B1pos1[0]
        self.B1_endpos = self.B1pos2[-1]
        self.B1_region = '{}:{}-{}'.format(self.chromosome, str(self.B1_startpos), str(self.B1_endpos))
        with open(self.expdat2B) as f:
            self.data2B = [line.rstrip('\n') for line in f]
        self.B2pos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data2B]
        self.B2pos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data2B]
        self.B2_startpos = self.B2pos1[0]
        self.B2_endpos = self.B2pos2[-1]
        self.B2_region = '{}:{}-{}'.format(self.chromosome, str(self.B2_startpos), str(self.B2_endpos))
        with open(self.cdat) as c1:
            self.cdata = [line.rstrip('\n') for line in c1]
        self.cpos1 = [int(line.split(',')[0].split('-')[0]) for line in self.cdata]
        self.cpos2 = [int(line.split(',')[0].split('-')[1]) for line in self.cdata]
        self.c_startpos = self.cpos1[0]
        self.c_endpos = self.cpos2[-1]
        self.c_region = '{}:{}-{}'.format(self.chromosome, str(self.c_startpos), str(self.c_endpos))
        with open(self.simdat) as f2:
            self.data2 = [line.rstrip('\n') for line in f2 if not line.startswith('region')]
        self.simpos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data2]
        self.simpos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data2]
        self.sim_startpos = self.simpos1[0]
        self.sim_endpos = self.simpos2[-1]
        self.sim_region = '{}:{}-{}'.format(self.chromosome, str(self.sim_startpos), str(self.sim_endpos))

        if self.A1_region == self.sim_region:
            if self.c_region == self.sim_region:
                self.region = self.A1_region
            else:
                print("Problem")
                quit()
        else:
            print('Problem')
            quit()
        self.A1_dict = {idx: None for idx, col in enumerate(self.data1A[0].split(','))}
        del self.A1_dict[0]
        for key in self.A1_dict.keys():
            fst_list = list()
            for line in self.data1A:
                fst_list.append(round(float(line.split(',')[key]), 4))
            self.A1_dict[key] = fst_list
        self.A2_dict = {idx: None for idx, col in enumerate(self.data2A[0].split(','))}
        del self.A2_dict[0]
        for key in self.A2_dict.keys():
            fst_list = list()
            for line in self.data2A:
                fst_list.append(round(float(line.split(',')[key]), 4))
            self.A2_dict[key] = fst_list
        self.B1_dict = {idx: None for idx, col in enumerate(self.data1B[0].split(','))}
        del self.B1_dict[0]
        for key in self.B1_dict.keys():
            fst_list = list()
            for line in self.data1B:
                fst_list.append(round(float(line.split(',')[key]), 4))
            self.B1_dict[key] = fst_list
        self.B2_dict = {idx: None for idx, col in enumerate(self.data2B[0].split(','))}
        del self.B2_dict[0]
        for key in self.B2_dict.keys():
            fst_list = list()
            for line in self.data2B:
                fst_list.append(round(float(line.split(',')[key]), 4))
            self.B2_dict[key] = fst_list
        self.c_dict = {idx: None for idx, col in enumerate(self.cdata[0].split(','))}
        del self.c_dict[0]
        for key in self.c_dict.keys():
            c_fst_list = list()
            for line in self.data2:
                c_fst_list.append(round(float(line.split(',')[key]), 4))
            self.c_dict[key] = c_fst_list
        self.sim_dict = {idx: None for idx, col in enumerate(self.data2[0].split(','))}
        del self.sim_dict[0]
        for key in self.sim_dict.keys():
            sim_fst_list = list()
            for line in self.data2:
                sim_fst_list.append(round(float(line.split(',')[key]), 4))
            self.sim_dict[key] = sim_fst_list

        self.range_list = list()
        for a, b in zip(self.A1pos1, self.A1pos2):
            # subtract 1, so that range
            self.range_list.append(range(a, b))
        self.outputfile = 'Fst_data.png'
        self.title = 'Simulated/Control Divergence vs. Experimental Divergence    {}'.format(self.region)
        self.x_label = 'Genomic Coordinate'
        # TODO: need to add variance to Fst when calculating so you can make error bars in graph (possibly)
        self.y_label = 'Fst (mean value for simulation data)'
        self.fig = None
        self.ax = None
        self.ymax = None
        self.colormap1 = ['lavender', 'honeydew', 'honeydew']
        self.colormap2 = ['chartreuse']
        self.colormap3 = ['darkorange']
        self.colormap4 = ['chartreuse']
        self.colormap5 = ['violet']
        self.colormap6 = ['violet']

    def find_ymax(self):
        max_val = 0
        for key in self.A1_dict.keys():
            freqs_check = self.A1_dict[key]
            new_max = round(max(freqs_check), 2)
            if new_max > max_val:
                max_val = new_max
        for key in self.A2_dict.keys():
            freqs2_check = self.A2_dict[key]
            new_max = round(max(freqs2_check), 2)
            if new_max > max_val:
                max_val = new_max
        for key in self.B1_dict.keys():
            freqs3_check = self.B1_dict[key]
            new_max = round(max(freqs3_check), 2)
            if new_max > max_val:
                max_val = new_max
        for key in self.B2_dict.keys():
            freqs4_check = self.B2_dict[key]
            new_max = round(max(freqs4_check), 2)
            if new_max > max_val:
                max_val = new_max
        for key in self.sim_dict.keys():
            chekker = self.sim_dict[key]
            new_max2 = round(max(chekker), 2)
            if new_max2 > max_val:
                max_val = new_max2
        for key in self.c_dict.keys():
            chekker2 = self.c_dict[key]
            new_max3 = round(max(chekker2), 2)
            if new_max3 > max_val:
                max_val = new_max3
        self.ymax = round(max_val, 2)
        # print(str(self.ymax))

    def plot(self):
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 10))
        self.ax.set_ylim([0, self.ymax + 0.05])
        xlim = len(range(1, 1000)) * len(self.range_list)
        self.ax.set_xlim([1, xlim])
        self.ax.set_title(self.title, fontsize=20)
        for key, color_iterator in zip(self.A1_dict.keys(), self.colormap2):
            y_data = list()
            for rng, freq in zip(self.range_list, self.A1_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, linewidth=5.0)
        for key, color_iterator in zip(self.A2_dict.keys(), self.colormap4):
            y_data = list()
            for rng, freq in zip(self.range_list, self.A2_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, alpha=0.5, linewidth=5.0)
        for key, color_iterator in zip(self.B1_dict.keys(), self.colormap5):
            y_data = list()
            for rng, freq in zip(self.range_list, self.B1_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, linewidth=5.0)
        for key, color_iterator in zip(self.B2_dict.keys(), self.colormap6):
            y_data = list()
            for rng, freq in zip(self.range_list, self.B2_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, alpha=0.5, linewidth=5.0)
        for key, color_iterator in zip(self.sim_dict.keys(), self.colormap1):
            y_data = list()
            for rng, freq in zip(self.range_list, self.sim_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, linestyle='dashed', linewidth=5.0)
        for key, color_iterator in zip(self.c_dict.keys(), self.colormap3):
            y_data = list()
            for rng, freq in zip(self.range_list, self.c_dict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            self.ax.plot(range(1, xlim + 1), y_data, color=color_iterator, alpha=0.5, linewidth=5.0)

        custom_lines = [Line2D([0], [0], color='chartreuse', lw=4, label='A Replicates'),
                        Line2D([0], [0], color='violet', lw=4, label='B Replicates'),
                        Line2D([0], [0], color='darkorange', lw=4, alpha=0.5, label='Controls'),
                        Line2D([0], [0], color='honeydew', lw=4, linestyle='dashed', label='Simulated')]
        # self.ax.set_xticks([idx for idx, s in enumerate(self.positions)])
        xticks = list(range(1, xlim, 1000))
        xticklables = ["{:,}".format(x) for x in self.A1pos1]
        # yrange = range(0, self.ymax + 0.05, 0)
        # yticks = [0.2, 0.4, 0.6, 0.8]
        # yticklabels = ['0.2', '0.4', '0.6', '0.8']
        legen = self.ax.legend(handles=custom_lines, loc='upper left')
        plt.setp(legen.get_texts(), color='w')

        self.ax.set_xticks(xticks[0::4])
        self.ax.set_xticklabels(xticklables[0::4])
        plt.setp(self.ax.get_xticklabels(), fontsize=15)
        plt.setp(self.ax.get_yticklabels(), fontsize=15)
        self.ax.set_ylabel('Fst', fontsize=18)
        self.ax.set_xlabel(self.x_label, fontsize=16)


if __name__ == '__main__':
    test = FstClass("/home/solid-snake/Data/mel_simulations2018/2R/testdat/2R_5000000-7000000_Fst", '2R')
    test.find_ymax()
    test.plot()
    test.fig.savefig('2R_5Mbp-7Mbp_Up_v_Down_1A_fst.png', bbox_inches='tight')
