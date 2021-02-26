"""  List the files that will be used make data for graphing """
import glob
import organize.directorymaker as mydir


class EndFreqs:

    def __init__(self, blueprint):
        all_freqs = glob.glob('{}/*end*/*.freqs'.format(mydir.main_dir(blueprint)))
        self.freq_dict = {'Gen15Up1A': None, 'Gen15Up2A': None,
                          'Gen15Dwn1A': None, 'Gen15Dwn2A': None,
                          'Gen15CtrlA': None,
                          'Gen15Up1B': None, 'Gen15Up2B': None,
                          'Gen15Dwn1B': None, 'Gen15Dwn2B': None,
                          'Gen15CtrlB': None}
        for key in self.freq_dict.keys():
            files = [s for s in all_freqs if '_Gen15_{}'.format(key) in s]
            files.sort(key=lambda x: int(x.split('/')[2].split('_')[0].split('-')[0]))
            self.freq_dict[key] = files
        self.output_files = list()

    def combine(self):
        for key, files in self.freq_dict.items():
            self.output_files.append('{}_combined.freqs'.format(key))
            with open('{}_combined.freqs'.format(key), 'w+') as output:
                for file in files:
                    position = file.split('/')[2].split('_')[0].split('-')[0]
                    mean_line = [line for line in open(file) if line.startswith('mean')][0]
                    output.write('{},{}'.format(position, ','.join(mean_line.split(',')[3:])))

    def return_files(self):
        """Outputs the list of combined files"""
        return self.output_files + ['Gen0A_combined.freqs', 'Gen0B_combined.freqs']


if __name__ == '__main__':
    pass
