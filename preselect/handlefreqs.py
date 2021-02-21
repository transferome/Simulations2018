"""Test modules and functions within"""
import glob


class SplitFreqs:
    """Split up frequency files into smaller windows which no-recombination
    should occur"""

    def __init__(self, blueprint_file):
        """Set up instance"""
        self.blueprint_file = blueprint_file
        self.freq_repA = glob.glob('*_Gen0RepAMaster.freqs')[0]
        self.freq_repB = glob.glob('*_Gen0RepBMaster.freqs')[0]
        self.window_list = list()

    def get_windows(self):
        """Get the windows to estimate haplotype frequencies in"""
        with open(self.blueprint_file) as blue_file:
            for line in blue_file:
                window = line.split(',')[0].split(':')[1]
                position1 = int(window.split('-')[0])
                position2 = int(window.split('-')[1])
                segment_range = range(position1, position2)
                segment_length = len(range(position1, position2))
                # position1_upstream = position1 + round(segment_length * 0.25)
                # position2_downstream = position2 - round(segment_length * 0.25)
                # self.window_list.append((position1, position2, segment_range, segment_length))
                self.window_list.append((position1, position2, segment_range, segment_length))

    def write(self, infile, outfile, window):
        """Write out subset file"""
        with open(infile) as freq, open(outfile, 'w+') as sub:
            for line in freq:
                split_line = line.split(' ')
                test_range = range(int(split_line[1]), int(split_line[2]))
                window_range = window[2]
                overlap_amount = len(range(max(window_range[0], test_range[0]), min(window_range[-1], test_range[-1]) + 1))
                overlap_percentage = round(overlap_amount/window[3], 2)
                # if window[2] in test_range and window[3] in test_range:
                if overlap_percentage > 0.74:
                    temp_line = line.split(' ')[:-1]
                    sub.write('{}\n'.format(','.join(temp_line)))

    def subset(self, window, replicate='A'):
        """Subsets the frequency file given a window, and replicate info"""
        if replicate == 'A':
            infile = self.freq_repA
            outfile = '{}-{}_Gen0RepA.freqs'.format(str(window[0]), str(window[1]))
            self.write(infile, outfile, window)
        elif replicate == 'B':
            infile = self.freq_repB
            outfile = '{}-{}_Gen0RepB.freqs'.format(str(window[0]), str(window[1]))
            self.write(infile, outfile, window)
        else:
            exit()

    def split(self, replicate='A'):
        """Main function to split up freqs for smaller sub regions"""
        self.get_windows()
        if replicate == 'A':
            for win in self.window_list:
                self.subset(win, replicate='A')
        elif replicate == 'B':
            for win in self.window_list:
                self.subset(win, replicate='B')
        else:
            exit()

    def gatherfreq(self, replicate='A'):
        """list either all of the A replicate freq files or the B replicate freq files"""
        fstart = open('replicate{}_frequencies.txt'.format(replicate), 'w+')
        fstart.close()
        freqs = glob.glob('*Rep{}.freqs'.format(replicate))
        for freq in freqs:
            with open('replicate{}_frequencies.txt'.format(replicate), 'a') as f1, open(freq) as f2:
                frequencies = [line.rstrip('\n') for line in f2 if line.startswith('mean')][0]
                frequencies = frequencies.split(',')[3:]
                regawn = freq.split('_')[0]
                f1.write('{}\n'.format(','.join([regawn] + frequencies)))


def endfiledict():
    # this dictionary guides the organization of the estimated frequencies at Gen15
    outfile_dict = {'Gen15Up1A': None, 'Gen15Up2A': None,
                    'Gen15Dwn1A': None, 'Gen15Dwn2A': None,
                    'Gen15CtrlA': None,
                    'Gen15Up1B': None, 'Gen15Up2B': None,
                    'Gen15Dwn1B': None, 'Gen15Dwn2B': None,
                    'Gen15CtrlB': None}
    outfiles = ['end{}_frequencies.txt'.format(key) for key in outfile_dict.keys()]
    for key in outfile_dict.keys():
        dictfile = [file for file in outfiles if key in file][0]
        outfile_dict[key] = dictfile
    return outfile_dict


class SplitEnds(SplitFreqs):
    """Sorts result of the Generation15 harp frequencies"""

    def __init__(self, blueprint):
        super(SplitEnds, self).__init__(blueprint)
        self.blueprint_file = blueprint
        self.freq = glob.glob('*Gen15*.freqs')
        self.sampledict = {'Gen15Up1A': None, 'Gen15Up2A': None,
                           'Gen15Dwn1A': None, 'Gen15Dwn2A': None,
                           'Gen15CtrlA': None,
                           'Gen15Up1B': None, 'Gen15Up2B': None,
                           'Gen15Dwn1B': None, 'Gen15Dwn2B': None,
                           'Gen15CtrlB': None}
        for key in self.sampledict.keys():
            freqfile = [file for file in self.freq if key in file]
            self.sampledict[key] = freqfile[0]
        self.window_list = list()
        self.endict = endfiledict()

    def subset_end(self, window):
        """Subsets the frequency file given a window, and replicate info"""
        for key in self.sampledict.keys():
            infile = self.sampledict[key]
            outfile = '{}-{}_Gen15_{}.freqs'.format(str(window[0]), str(window[1]), key)
            self.write(infile, outfile, window)

    def split_end(self):
        """ Splits the windows and sample types"""
        self.get_windows()
        for win in self.window_list:
            self.subset_end(win)

    def gather_end(self):
        """list either all of the A replicate freq files or the B replicate freq files"""
        for key in self.sampledict.keys():
            fout = self.endict[key]
            freqs = glob.glob('*{}*.freqs'.format(key))
            # this will remove files that were used to create the subset region freq files
            freqs = [file for file in freqs if ":" not in file]
            outputlist = list()
            for freq in freqs:
                with open(freq) as f2:
                    frequencies = [line.rstrip('\n') for line in f2 if line.startswith('mean')][0]
                    frequencies = frequencies.split(',')[3:]
                    regawn = freq.split('_')[0]
                    outputlist.append('{}\n'.format(','.join([regawn] + frequencies)))
            outputlist.sort(key=lambda x: int(x.split(',')[0].split('-')[0]))
            with open(fout, 'w+') as f1:
                for line in outputlist:
                    f1.write(line)


if __name__ == '__main__':
    pass
