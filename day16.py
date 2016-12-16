from copy import copy


def _chk(data, L):
    print('Generating dragon data...')
    while len(data) < L:
        data = _dragon(data)
    data = data[:L]
    print('Done!')

    print('Creating checksum...')
    if len(data) % 2 > 0:
        chk = copy(data)
    else:
        chk = ''.join(['1' if a == b else '0'
                       for (a, b) in zip(data[::2], data[1::2])])
    print('Done!')

    print('Hashing checksum...')
    while len(chk) % 2 == 0:
        chk = ''.join(['1' if a == b else '0'
                       for (a, b) in zip(chk[::2], chk[1::2])])
    print('Done!')
    return chk


def _dragon(a):
    b = ['1' if aj == '0' else '0' for aj in a[::-1]]
    return a + '0' + ''.join(b)

if __name__ == "__main__":
    input = '10010000000110000'
    L1 = 272
    chk1 = _chk(input, L1)

    print('\nPart 1')
    print('\tLength of chk is: {}'.format(len(chk1)))  # expect 17
    print('\tValue of chk is: {}'.format(chk1))
    # 10010110010011110

    L2 = 35651584
    chk2 = _chk(input, L2)

    print('\nPart 2')
    print('\tLength of chk is: {}'.format(len(chk2)))
    print('\tValue of chk is: {}'.format(chk2))
    # 01101011101100011
