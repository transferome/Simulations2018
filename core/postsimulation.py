"""  Some processes to do once all the simulations have completed  """
import fst.fstbetweenreplicate as fstbetweenf
import fst.avgfst as avg


def fst_bewtweenreplicate():
    fstbetweenf.fst_between()


def average_fst(blueprint):
    avgblp = avg.AvgFst(blueprint)
    avgblp.files_regions()
    avgblp.gather_data()
    avgblp.write_sum()


if __name__ == '__main__':
    pass
