""" Reads in a harp.freq file and extracts data """


def lines_create(file, arm_type='2R'):
    """Reads in dgrp_line header from a snp file, header is always the same so this function
    needs no arguments"""
    if 'X' not in arm_type:
        dgrp_lines = [line.rstrip('\n') for line in open(file)][0][7:]
        return dgrp_lines.split(',')
    else:
        dgrp_lines = [line.rstrip('\n') for line in open(file)][0][6:]
        return dgrp_lines.split(',')


def read_freq(filename):
    """Reads in frequency file, stripping off the new line character"""
    return_list = list()
    for line in open(filename):
        if '-nan' in line:
            line_n = line.rstrip(' \n')
            line_split = line_n.split(' ')
            line_start = ' '.join(line_split[0:3])
            fill_zeroes = ' '.join(['0' for s in line_split if '-nan' in s])
            new_line = '{} {}'.format(line_start, fill_zeroes)
            return_list.append(new_line)
        else:
            line_f = line.rstrip(' \n')
            return_list.append(line_f)
    return return_list


def freq_split(freq_data, chromosome):
    """Removes chromosome info, places - between the two coordinates, and splits the coordinate
    info from the frequency data"""
    chromosome_replace = '{} '.format(chromosome)
    return [tuple(line.replace(chromosome_replace, '').replace(' ', '-', 1).split(' ', 1)) for line
            in freq_data]


def region_intervals(split_list):
    """Makes a list of only the region info"""
    return [item[0] for item in split_list]


def region_data_dictionary(split_list, line_list):
    """Makes a dictionary which has the hyphenated coordinates as keys, and the line of data for
    that region as values"""
    output_dictionary = {}
    for item in split_list:
        split_frequencies = item[1].split(' ')
        output_dictionary[item[0]] = zip(line_list, split_frequencies)
    return output_dictionary


def create_dummy_dictionary(line_list, region_list):
    """Makes a nested dummy dictionary with lines as the first set of keys, and then the
    hyphenated region coordinates as the second set of keys, temporarily putting None for all
    values"""
    none_holder = [None for _ in range(len(region_list))]
    output_dictionary = {}
    for line in line_list:
        output_dictionary[line] = dict(zip(region_list, none_holder))
    return output_dictionary


def fill_dummy_dictionary(data_dictionary, dummy_dictionary):
    """Fills in the dummy dictionary with data using the return region_data_dictionary"""
    for region in list(data_dictionary.keys()):
        data_line = data_dictionary[region]
        for item in data_line:
            line_key = item[0]
            dummy_dictionary[line_key][region] = item[1]
    return dummy_dictionary


def new_dataframe(region_list, filled_dictionary, line_list, sample_info):
    """Creates new dataframe using the filled_dictionary and the dgrp line list.  Also will take
    sample info at some point"""
    header = region_list
    header.insert(0, 'line_num')
    header.insert(1, 'sample')
    # header.append('\n')
    header = '{}\n'.format('\t'.join(header))
    out_list = list()
    out_list.append(header)
    for line in line_list:
        line_dict = filled_dictionary[line]
        data_row = list(line_dict.values())
        data_row.insert(0, line)
        data_row.insert(1, sample_info)
        # data_row.append('\n')
        data_row = '{}\n'.format('\t'.join(data_row))
        out_list.append(data_row)
    return out_list


def write_new_dataframe(new_data, new_file):
    """Write new data to a txt file"""
    with open(new_file, 'w+') as f:
        for line in new_data:
            f.write(line)


if __name__ == '__main__':
    samples = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S21', 'S22']
    contig = '3R'
    step = '100k'
    for sample in samples:
        freq_input = "{}_{}step/{}_{}.freqs".format(contig, step, sample, contig)
        new_output = '{}.txt'.format(freq_input.split('.freqs')[0])
        # directory from personal PC
        lines = lines_create("/home/nala/Dropbox/PyCharm_Reseq/DGRPvcf/TextFiles/SNP_txt_Harp/{}_snp_good.txt".format(contig), contig)
        df = read_freq(freq_input)
        df_split = freq_split(df, contig)
        regions = region_intervals(df_split)
        data_dict = region_data_dictionary(df_split, lines)
        dum_dict = create_dummy_dictionary(lines, regions)
        fill_dict = fill_dummy_dictionary(data_dict, dum_dict)
        new_df = new_dataframe(regions, fill_dict, lines, '{}_{}'.format(sample, contig))
        write_new_dataframe(new_df, new_output)
