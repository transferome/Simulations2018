"""Test modules and functions within"""
# import preselect.harpsnp.sumfreq as summer
#
# test = summer.read_freq('2R', '8000000-8097009_Gen0RepA.freqs')
# mean_vals = test.mean(axis=0).tolist()
# mean = ["{:.5f}".format(float(num)) for num in mean_vals]
# mean.insert(0, 'mean')
# var_vals = test.var(axis=0).tolist()
# var = ["{:.8f}".format(float(num)) for num in var_vals]
# var.insert(0, 'var')
#
# test.loc[len(test.index)] = mean
# test.loc[len(test.index)] = var
#
# test.to_csv(path_or_buf='8000000-8097009_Gen0RepA.freqs', sep=',', header=True, index=False)
#
import numpy as np

dat = [line for line in open('replicateA_frequencies.txt')]
dat
test = dat[0].rstrip('\n').split(',')[1:]
numt = [float(x) for x in test]
sum(numt)
normt = [x/sum(numt) for x in numt]
tot = np.random.multinomial(2000, normt, 10)
len(tot[1])