from hashlib import md5
from collections import deque




def has_tuplet(string, t=3):
    for j in range(len(string)+1-t):
        # print(string[j])
        if all(string[j] == string[k] for k in range(j+1, j+t)):
            return string[j]
    return


def has_matching_tuplet(string, letter, t=5):
    letter2 = has_tuplet(string, t)
    if letter2 is None:
        return False
    elif not letter == letter2:
        ltr_idx = string.index(letter2)
        return has_matching_tuplet(string[ltr_idx+t:], letter, t)
    else:
        return True


def md5hash(pz, idx):
    return md5((pzinput+str(idx)).encode('utf-8')).hexdigest()


def hash2016(x):
    result = x
    for _ in range(2016):
        result = md5(result.encode('utf-8')).hexdigest()
    return result


def _main(pz, part2=False):
    # for memoization
    hash_deque = deque()
    memo3 = deque()
    memo5 = deque()
    pad_keys = deque()

    idx = 0
    memoidx = 0
    while len(pad_keys) < 64:
        if part2:
            hash_deque.append(hash2016(md5hash(pz, idx)))
        else:
            hash_deque.append(md5hash(pz, idx))
        hash_idx = hash_deque[-1]
        trp_let = has_tuplet(hash_idx, 3)
        pnt_let = has_tuplet(hash_idx, 5)
        memo3.append(trp_let)
        memo5.append(pnt_let)
        if idx > memoidx + 1000:
            if memo3[memoidx]:
                nextThou = (j for j in range(memoidx + 1, memoidx + 1001)
                            if memo5[j])
                tuples = (has_matching_tuplet(hash_deque[j], memo3[memoidx], 5)
                          for j in nextThou)
                if any(tuples):
                    pad_keys.append(memoidx)
            memoidx += 1
        idx += 1
    return pad_keys

if __name__ == "__main__":
    do_test_cases = False
    do_p1 = True
    do_p2 = True

    pzinput = 'zpqevtbw'

    # # # Test cases # # #
    if do_test_cases:
        duplet1 = 'aaron'
        duplet2 = 'onaar'
        duplet3 = 'ronaa'

        triplet1 = 'aaaron'
        triplet2 = 'onaaar'
        triplet3 = 'ronaaa'

        hexlet1 = 'assssssdffffffab'
        nopelet = 'asdfjklglajsdkle'

        print('Duplets:')
        for d in [duplet1, duplet2, duplet3]:
            print(d)
            print(has_tuplet(d, 1))
            print(has_tuplet(d, 2))
            print(has_tuplet(d, 3))

        print('Triplets:')
        for d in [triplet1, triplet2, triplet3]:
            print(d)
            print(has_tuplet(d, 3))

        print('Weirds:')
        for d in [hexlet1, nopelet]:
            print(d)
            print(has_matching_tuplet(d, 'f', 5))

    if do_p1:
        print('Part 1:')
        pad_keys = _main(pzinput)
        print(pad_keys)

    if do_p2:
        print('Part 2:')
        pad_keys = _main(pzinput, True)
        print(pad_keys)
