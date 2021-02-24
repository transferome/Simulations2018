"""  Make data from the frequency file so it can be graphed.
This will take the list of returned files from the EndFreqs objects in combinedfreqs.py"""


def position_guide(filename):
    """Gets the list of positions from the file"""
    with open(filename) as f:
        positions = [int(line.split(',')[0]) for line in filename]
        position_start = positions[0]
        position_end = positions[-1]
        # not going to add 1, that way x coordinates won't double up
        interval_length = len(range(position_start, position_end))

