import pandas as pd
import numpy as np
import scipy.stats as stats


ab = 'abcdefghijklmnopqrstuvwxyz'


def _getMode(vec):
    nums = [ab.index(x) for x in vec]
    return ab[stats.mode(nums).mode[0]]


def _getLetterCounts(npvec):
    return [''.join(npvec.tolist()).count(ell) for ell in ab]


def _getUnmode(npvec):
    # vec is a list
    return(ab[np.argmin(_getLetterCounts(npvec))])


if __name__ == "__main__":
    data = pd.read_csv('./input/day6input.csv', sep=' ', header=None)
    data = data.values  # rows are short; want mode of each column
    outputcode = []
    for k in range(data.shape[1]):
        outputcode.append(_getMode(data[:, k]))
    print('Answer for part 1:')
    print(''.join(outputcode))

    print('Answer for part 2:')
    outputcode = []
    for k in range(data.shape[1]):
        outputcode.append(_getUnmode(data[:, k]))
    print(''.join(outputcode))
