from load_data import load_data
from pprint import pprint


def isTr(l, c, r):
    return ((l and c and not r) or
            (c and r and not l) or
            (l and not (c or r)) or
            (r and not (c or l)))


# True if trap false otherwise.
def gnr(c):
    d = [False, *c, False]
    return [True if isTr(d[j-1], d[j], d[j+1]) else False
            for j in range(1, len(d)-1)]


def count(d):
    return sum(1 for s in d if not s)


def toBool(dChar):
    return [True if s == '^' else False for s in dChar]


def toChar(dBool):
    return ''.join(['^' if s else '.' for s in dBool])


if __name__ == "__main__":
    PRINT_OUTPUT = True

    tdata = ['.^^.^.^^^^']
    tbool = [toBool(d) for d in tdata]
    numrowst = 10
    print('Test data')
    while len(tbool) < numrowst:
        tbool.append(gnr(tbool[-1]))
    pprint([toChar(d) for d in tbool])
    print()

    data1 = load_data('./input/day18.txt')
    data1[0] = toBool(data1[0])

    data2 = load_data('./input/day18.txt')
    data2 = toBool(data2[0])

    numrows1 = 40
    numrows2 = 400000

    print('Part 1')
    while len(data1) < numrows1:
        data1.append(gnr(data1[-1]))

    if PRINT_OUTPUT:
        # Sierpinski triangles
        pprint([toChar(d) for d in data1], compact=True)
    print('\tNumber of safe tiles: {}.'.format(sum(count(d) for d in data1)))

    print('\nPart 2')
    L = 1
    ctr = count(data2)
    while L < numrows2:
        data2 = gnr(data2)
        ctr += count(data2)
        L += 1

    if PRINT_OUTPUT:
        print(toChar(data2))
    print('\tNumber of safe tiles: {}.'.format(ctr))

# Answer for part 1: 1974
# Answer for part 2: 19991126
