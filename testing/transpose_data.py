"""Function to Tranpose a Dataframe, it will make the columns the rows, and the rows the columns.  Written/Tested with
python --version 3.7"""
import numpy as np


def txt_to_list(filename):
    """Function reads in \t delimited text file, and creates a nested list.  Each item in the list, is a list which is a
     line split into a list by the \t delimiter"""
    txt_list = list()
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line_as_list = line.split(',')
            txt_list.append(line_as_list)
    return txt_list


def check_list_lengths(txt_to_list_data):
    """Check if all lines, have the same number of elements in their lists"""
    tester_list = [len(x) == len(txt_to_list_data[0]) for x in txt_to_list_data]
    return all(tester_list)


def transpose_data(txt_to_list_data):
    """Transforms data so that rows are columns, and columns are rows"""
    # convert our nested list into a numpy array
    data_array = np.array(txt_to_list_data)
    data_transposed = data_array.transpose()
    transposed_data = data_transposed.tolist()
    # and now let's join lines back together with '\t', and add new lines to the end of each of the new rows
    return [','.join(line_list[1:]) + '\n' for line_list in transposed_data]


# def write_text(filename, txt_list):
#     """Given a filename, writes lines of text to a file as is"""
#     with open('{}_trapnspose.txt'.format(filename.split('.txt')[0]), 'w+') as f:
#         for line in txt_list[1:]:
#             f.write(line)


def convert(filename):
    text_data = txt_to_list(filename)
    check_list_lengths(text_data)
    trans = transpose_data(text_data)
    # write_text(filename, trans)
    return trans[1:]


if __name__ == '__main__':
    pass
