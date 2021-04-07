"""  Dictionary which gets the number of times identical strings exist within a list """


def duplicate_counter(input_list):
    """Creates a dictionary with each list element as a key, and value as 1, but if the
    list element (key) is repeated, the value of 1 is increased by 1, thus counting the
    number of times each element is duplicated in the list, if any key in the dictionary
    has a value over 1"""
    element_dictionary = {}
    for element in input_list:
        if element in element_dictionary:
            element_dictionary[element] += 1
        else:
            element_dictionary[element] = 1
    # keeping only duplicated values ( number of haplotypes with more than 1 entry)
    duplicate_number = [value for value in element_dictionary.values() if value > 1]
    # total number of unique haplotypes is the number of keys in dictionary
    key_number = len(element_dictionary.keys())
    # percentage of haplotypes which are multiples, is duplicate_number divided by key_number
    return len(duplicate_number)/key_number, key_number


if __name__ == '__main__':
    pass
