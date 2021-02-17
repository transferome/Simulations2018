"""Test modules and functions within"""

# dat = [line for line in open('8000000-8097009_RepA_simulations.freqs')]
#
# line1 = dat[1].rstrip('\n').split(',')[1:]
# line2 = dat[2].rstrip('\n').split(',')[1:]
#
# with open('8000000-8097009_RepA_simulations.freqs') as file:
#     data = [line.rstrip('\n') for line in file][1:]
#     # make the list missing the start, and another missing the end
#     output_list = list()
#     for idx, line in enumerate(data, 1):
#         if not idx % 2 == 0:
#             pair = (line, data[idx])
#             output_list.append(pair)
#         else:
#             pass
#
# output_list
#
# fst(line1, line2)