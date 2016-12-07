# Day 7 of the Advent of Code

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import hashlib as hl


def palindrome_indices(s):
    # s is input string
    print(s)
    idx = [j-1 for j in range(1, len(s)-2)
           if (s[j] == s[j+1])
           and s[j-1] == s[j+2]
           and not (s[j-1] == s[j])]
    return idx

def bracket_indices(s):
    idxL = [j for j in range(len(s)) if s[j] is '[']
    idxR = [j for j in range(len(s)) if s[j] is ']']
    idxZ = [(j, k) for j, k in zip(idxL, idxR)]
    # print(idxZ)
    return idxZ


def isBetweenBrackets(pidx, bracket_indices):
    # pidx is the index of a palindrome
    return any([pidx > bidx[0] and pidx < bidx[1]
                for bidx in bracket_indices])


def validABBA(s):
    pdromeidx = palindrome_indices(s)
    bidx = bracket_indices(s)
    L = len(pdromeidx)
    bt_brackets = [isBetweenBrackets(p, bidx) for p in pdromeidx]
    if L == 0 or any(bt_brackets):
        return False
    else:
        return L > 0


def _main(data):
    results = 0 
    for d in data:
        if validABBA(d):
            results += 1
    return results


if __name__ == "__main__":
    with open('./input/day7input.csv', 'r') as fp:
        read_data = fp.read()

    data = read_data.split('\n')[:-1]
    print(data[0])

    results = _main(data)
    print('Answer for first part is:')
    print(results)
