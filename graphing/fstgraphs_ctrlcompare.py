"""  Module  """
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
    "xtick.color": "goldenrod",
    "ytick.color": "goldenrod",
    "grid.color": "black",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "font.monospace": "monospace",
    "savefig.edgecolor": "black",
    "figure.max_open_warning": 0})


class FstData:
    def __init__(self, fstfile, chromosome, simulated=False):
        self.data = None
        if not simulated:
            with open(fstfile) as f:
                self.data = [line.rstrip('\n') for line in f]
        else:
            with open(fstfile) as f:
                self.data = [line.rstrip('\n') for line in f if not line.startswith('region')]
        self.pos1 = [int(line.split(',')[0].split('-')[0]) for line in self.data]
        self.pos2 = [int(line.split(',')[0].split('-')[1]) for line in self.data]
        self.startpos = self.pos1[0]
        self.endpos = self.pos2[-1]
        self.region = '{}:{}-{}'.format(chromosome, str(self.startpos), str(self.endpos))
        self.dict = None

    def dictionary(self):
        self.dict = {idx: None for idx, col in enumerate(self.data[0].split(','))}
        del self.dict[0]
        for key in self.dict.keys():
            fst_list = list()
            for line in self.data:
                fst_list.append(round(float(line.split(',')[key]), 4))
            self.dict[key] = fst_list

    def max(self, maxval):
        tracker = maxval
        for key in self.dict.keys():
            freqs_check = self.dict[key]
            new_max = round(max(freqs_check), 2)
            if new_max > tracker:
                tracker = new_max
        return tracker


class FstClass:

    def __init__(self, chromosome):
        """Gets the list of positions from the file"""
        self.chromosome = chromosome
        self.expdatA1 = 'Exp_Up1A_CtrlA_Fst.dat'
        self.expdatA2 = 'Exp_Up2A_CtrlA_Fst.dat'
        self.expdatB1 = 'Exp_Up1B_CtrlB_Fst.dat'
        self.expdatB2 = 'Exp_Up2B_CtrlB_Fst.dat'
        self.expdat
        self.cdat = 'Exp_CtrlA_CtrlB_Fst.dat'
        self.simdat = glob.glob('*_Simulation_Fst.dat')[0]
        self.region = None
        self.expdatA1obj = FstData(self.expdatA1, self.chromosome)
        self.expdatA2obj = FstData(self.expdatA2, self.chromosome)
        self.expdatB1obj = FstData(self.expdatB1, self.chromosome)
        self.expdatB2obj = FstData(self.expdatB2, self.chromosome)
        self.cdatobj = FstData(self.cdat, self.chromosome)
        self.simdatobj = FstData(self.simdat, self.chromosome, simulated=True)

        if self.expdatA1obj.region == self.simdatobj.region:
            if self.cdatobj.region == self.simdatobj.region:
                self.region = self.expdatA1obj.region
            else:
                print("Problem")
                quit()
        else:
            print('Problem')
            quit()
        self.expdatA1obj.dictionary()
        self.expdatA2obj.dictionary()
        self.expdatB1obj.dictionary()
        self.expdatB2obj.dictionary()
        self.cdatobj.dictionary()
        self.simdatobj.dictionary()

        self.range_list = list()
        for a, b in zip(self.expdatA1obj.pos1, self.expdatA1obj.pos2):
            # subtract 1, so that range
            self.range_list.append(range(a, b))
        self.outputfile = 'Fst_data.png'
        # self.title = 'Comparing Up & Down Haplotype Frequencies (1Kb windows)'
        self.x_label = 'Genomic Coordinate: Chromosome Arm {}'.format(self.chromosome)
        # TODO: need to add variance to Fst when calculating so you can make error bars in graph (possibly)
        self.y_label = 'Fst (Haplotype Frequencies in 100Kb windows)'
        self.fig = None
        self.ax = None
        self.ymax = None
        self.simcolormap = ['honeydew', 'honeydew', 'honeydew']
        self.expdatAcolormap = ['chartreuse']
        self.ctrlcolormap = ['orangered']
        self.expdatBcolormap = ['violet']

    def find_ymax(self):
        max_val = self.expdatA1obj.max(0)
        max_val = self.expdatA2obj.max(max_val)
        max_val = self.expdatB1obj.max(max_val)
        max_val = self.expdatB2obj.max(max_val)
        max_val = self.cdatobj.max(max_val)
        max_val = self.simdatobj.max(max_val)
        self.ymax = round(max_val, 2)
        # print(str(self.ymax))

    def easy_ymax(self):
        self.ymax = 0.95

    def plotfst(self, axis, datadict, coloriter, xlimit, alpha_val, linetype='-'):
        for key, color_iterator in zip(datadict.keys(), coloriter):
            y_data = list()
            for rng, freq in zip(self.range_list, datadict[key]):
                y_data.extend([freq for _ in range(1, 1000)])
            axis.plot(range(1, xlimit + 1), y_data, color=color_iterator, linestyle=linetype, alpha=alpha_val,
                      linewidth=5.0)

    def plot(self):
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 10))
        self.ax.set_ylim([0, self.ymax + 0.05])
        xlim = len(range(1, 1000)) * len(self.range_list)
        self.ax.set_xlim([1, xlim])
        # self.ax.set_title(self.title, fontsize=20)
        self.plotfst(self.ax, self.expdatA1obj.dict, self.expdatAcolormap, xlim, 1.0)
        self.plotfst(self.ax, self.expdatA2obj.dict, self.expdatAcolormap, xlim, 0.5)
        self.plotfst(self.ax, self.expdatB1obj.dict, self.expdatBcolormap, xlim, 1.0)
        self.plotfst(self.ax, self.expdatB2obj.dict, self.expdatBcolormap, xlim, 0.5)
        self.plotfst(self.ax, self.simdatobj.dict, self.simcolormap, xlim, 1.0, '--')
        self.plotfst(self.ax, self.cdatobj.dict, self.ctrlcolormap, xlim, 0.8)

        custom_lines = [Line2D([0], [0], color='chartreuse', lw=4, label='A Replicates'),
                        Line2D([0], [0], color='violet', lw=4, label='B Replicates'),
                        Line2D([0], [0], color='orangered', lw=4, alpha=0.8, label='Controls'),
                        Line2D([0], [0], color='honeydew', lw=4, linestyle='dashed', label='Simulated')]
        # self.ax.set_xticks([idx for idx, s in enumerate(self.positions)])
        xticks = list(range(1, xlim, 1000))
        xticklables = ["{:,}".format(x) for x in self.expdatA1obj.pos1]
        # yrange = range(0, self.ymax + 0.05, 0)
        # yticks = [0.2, 0.4, 0.6, 0.8]
        # yticklabels = ['0.2', '0.4', '0.6', '0.8']
        legen = self.ax.legend(fontsize=13, handles=custom_lines, loc='upper left')
        plt.setp(legen.get_texts(), color='w')

        self.ax.set_xticks(xticks[0::4])
        self.ax.set_xticklabels(xticklables[0::4])
        plt.setp(self.ax.get_xticklabels(), fontsize=13)
        plt.setp(self.ax.get_yticklabels(), fontsize=13)
        self.ax.set_ylabel(self.y_label, fontsize=17)
        self.ax.set_xlabel(self.x_label, fontsize=17)


if __name__ == '__main__':
    import os
    import glob

    contig = '3R'
    x1 = 7
    x2 = 9
    os.chdir(f'/home/solid-snake/Data/mel_simulations2018/{contig}/testdat/{contig}_{x1}000000-{x2}000000_Fst')
    plotobj = FstClass({contig})
    plotobj.easy_ymax()
    plotobj.plot()
    plotobj.fig.savefig(f'/home/solid-snake/Data/mel_simulations2018/{contig}/testdat/{contig}_{x1}Mbp-'
                        f'{x2}Mbp_Up_v_Down_Fst.png', bbox_inches='tight')
    plt.clf()