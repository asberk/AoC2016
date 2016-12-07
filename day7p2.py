
def bracket_indices(s):
    # finds all bracket pairs in a string s; returned as
    # [ [L1, R1], [L2, R2], ... ]
    idxL = [j for j in range(len(s)) if s[j] is '[']
    idxR = [j for j in range(len(s)) if s[j] is ']']
    idxZ = [(j, k) for j, k in zip(idxL, idxR)]
    # print(idxZ)
    return idxZ


def ABA_potentials(s):
    # s is input string; returns list of potential indices
    idx = [j-1 for j in range(1, len(s)-1)
           if (s[j-1] == s[j+1])
           and not (s[j-1] == s[j])
           and not ('[' in s[(j-1):(j+1)])
           and not (']' in s[(j-1):(j+1)])]
    return idx

def isBetweenBrackets(pidx, bracket_indices):
    # pidx is the index of a palindrome
    # bracket_indices is a list of pairs of bracket indices
    return any([pidx > bidx[0] and pidx < bidx[1]
                for bidx in bracket_indices])


def ABA_indices(s):
    potentials = ABA_potentials(s)
    bidx = bracket_indices(s)
    return [idx
            for idx in potentials
            if not isBetweenBrackets(idx, bidx)]


def BAB_potentials(s):
    return ABA_potentials(s)


def BAB_indices(s):
    potentials = BAB_potentials(s)
    bidx = bracket_indices(s)
    return [idx
            for idx in potentials
            if isBetweenBrackets(idx, bidx)]


def getSeq(s, idx, kind):
    # kind is one of 'aba' or 'bab'
    if kind is 'aba':
        ab = [(s[j], s[j+1]) for j in idx]
    elif kind is 'bab':
        ab = [(s[j+1], s[j]) for j in idx]
    else:
        raise Exception('wrong argument to kind')
    return ab


def valid_ABA_BAB(s):
    aba_idx = ABA_indices(s)
    bab_idx = BAB_indices(s)
    ab_aba = getSeq(s, aba_idx, 'aba')
    ab_bab = getSeq(s, bab_idx, 'bab')
    return any([x in ab_bab for x in ab_aba])


def _main(data):
    results = 0
    for d in data:
        if valid_ABA_BAB(d):
            results += 1
    return results

if __name__ == "__main__":
    with open('./input/day7input.csv', 'r') as fp:
        read_data = fp.read()

    data = read_data.split('\n')[:-1]
    print(data[0])

    results = _main(data)
    print('Answer to part 2:')
    print(results)

    # print('debugging...\n')

    # test1 = 'aba[bab]xyz'
    # test2 = 'xyx[xyx]xyx'
    # test3 = 'aaa[kek]eke'
    # test4 = 'zazbz[bzb]cdb'
    # for t in [test1, test2, test3, test4]:
    #     print(t)
    #     print(valid_ABA_BAB(t))
