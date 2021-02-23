"""Remove outputs produced by Harp"""
import glob
import shutil
import os
import organize.directorymaker as mydir


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
        hlk_files = glob.glob('*.hlk')
        for direct in output_directories:
            shutil.rmtree(direct)
            # print(direct)
        for file in hlk_files:
            os.remove(file)
            # print(file)

    def move_freq(self, blueprint):
        endfreq_directory = mydir.endfreq_dir(blueprint)
        freqs = glob.glob('*Gen15*.freqs')
        for freq in freqs:
            shutil.move(freq, endfreq_directory)


if __name__ == '__main__':
    pass
