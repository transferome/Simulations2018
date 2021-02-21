"""Remove outputs produced by Harp"""
import glob
import shutil
import os


class HarpClean:
    """Clean results of harp"""

    def __init__(self):
        output_directories = glob.glob('*Master.output')
        hlk_files = glob.glob('*.hlk')
        for direct in output_directories:
            shutil.rmtree(direct)
            # print(direct)
        for file in hlk_files:
            os.remove(file)
            # print(file)


class HarpSimClean(HarpClean):
    """Clean results of har simreads"""

    def __init__(self):
        super(HarpSimClean, self).__init__()
        output_directories = glob.glob('*.output')
        hlk_files = glob.glob('*.hlk')
        bam_files = glob.glob('*.bam*')
        for direct in output_directories:
            shutil.rmtree(direct)
            # print(direct)
        for file in hlk_files:
            os.remove(file)
            # print(file)
        for bam in bam_files:
            os.remove(bam)
            # print(bam)


class HarpEndClean(HarpClean):
    """Clean results of har simreads"""

    def __init__(self):
        super(HarpEndClean, self).__init__()
        output_directories = glob.glob('*Gen15*.output')
        self.freqs = glob.glob('*Gen15*.freqs')
        hlk_files = glob.glob('*.hlk')
        for direct in output_directories:
            shutil.rmtree(direct)
            # print(direct)
        for file in hlk_files:
            os.remove(file)
            # print(file)

    def clear_freq(self):
        for freq in self.freqs:
            os.remove(freq)


if __name__ == '__main__':
    pass
