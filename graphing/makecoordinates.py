"""  Make data from the frequency file so it can be graphed.
This will take the list of returned files from the EndFreqs objects in combinedfreqs.py"""


def position_guide(filename):
    """Gets the list of positions from the file"""
    with open(filename) as f:
        data = [line.rstrip('\n') for line in f]
    positions = [int(line.split(',')[0]) for line in data]
    # not going to add 1, that way x coordinates won't double up
    row_range_list = [range(position, positions[i + 1]) for i, position in enumerate(positions[:-1])]
    # need to add the range for the final element in positions list (last line of file)
    # adding length of a region (they're all the same) to achieve that
    row_range_list.append(range(positions[-1] + len(range(positions[0], positions[1]))))
    col_dict = {idx: None for idx, col in enumerate(data[0].split(','))}
    for key in col_dict.keys():
        freq_list = list()
        for line in data:
            freq_list.append(float(line.split(',')[key]))

        col_dict[key] = freq_list



