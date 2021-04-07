"""  Get the number of reads on average from the harp like process.
  These are giving the number of reads within a simulated bam that the harp
  like process handles"""
import glob


def list_summaries():
    """Lists the summary.txt files"""
    return glob.glob('*.output/like/*summary.txt')


def get_reads(summary_file):
    """Gets the number of pairs used in the harp likelihood process"""
    with open(summary_file) as f:
        temp_info = [line.rstrip('\n') for line in f if line.startswith('pairs_passed_filter:')][0]
        print(temp_info.split(': ')[1])
        return int(temp_info.split(': ')[1])


def mean_coverage():
    covlist = list()
    sumfiles = list_summaries()
    for file in sumfiles:
        covlist.append(get_reads(file))
    mincov = min(covlist)
    maxcov = max(covlist)
    meancov = sum(covlist)/len(covlist)
    print('Max:{}  Min:{}  Mean:{}'.format(str(maxcov), str(mincov), str(meancov)))


if __name__ == '__main__':
    mean_coverage()
