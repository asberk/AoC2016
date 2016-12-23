# # # #
# Advent of Code
# Day 23
# By: Aaron Berk
#
# Puzzle input:
# cpy 1 a
# cpy 1 b
# cpy 26 d
# jnz c 2
# jnz 1 5
# cpy 7 c
# inc d
# dec c
# jnz c -2
# cpy a c
# inc a
# dec b
# jnz b -2
# cpy c b
# dec d
# jnz d -6
# cpy 19 c
# cpy 14 d
# inc a
# dec d
# jnz d -2
# dec c
# jnz c -5
#
# Goal: find the value in register a
# Part (b): prepend the instruction "cpy 1 c"; same goal
#
# Descripton: A bare-bones compiler type thing with four registers.
# Answer for part (a): 318077
# Answer for part (b): 9227731
# # # #

from load_data import load_data


def add_check(d0, d1, d2):
    return (d2[0] == 'jnz' and d2[-1] == '-2' and
            (d0[0] in ['inc', 'dec'] and d1[0] in ['inc', 'dec']) and
            (d0[1] == d2[1] or d1[1] == d2[1]))


def add(r, d0, d1, d2, d3=None, d4=None):
    ff = {'inc': inc, 'dec': dec}
    if d2 is None:
        return ff[d0[0]](r, d0[1])
    else:
        ctr = d2[1]
        if d0[1] == ctr:  # then d0 is counter too
            if ((d0[0] == 'inc' and r[ctr] >= 0) or
                (d0[0] == 'dec' and r[ctr] <= 0)):
                raise Exception('This will not converge')
            elif multiply_check(r, d3, d4):
                r = multiply(r, d1[1], ctr, d3)
                return 5, r
            else:
                if d1[0] == 'inc':
                    r[d1[1]] += abs(r[ctr])
                    r[ctr] = 0
                elif d1[0] == 'dec':
                    r[d1[1]] -= abs(r[ctr])
                    r[ctr] = 0
                else:
                    raise ValueError('Unknown operation for d1')
                return 3, r
        elif d1[1] == d2[1]:  # switch 'em around and get the same result
            return add(r, d1, d0, d2, d3, d4)


def multiply_check(r, d3, d4):
    if d3 is None or d4 is None:
        return False
    else:
        return (d4[0] == 'jnz' and d4[-1] == '-5' and
                d3[0] in ['inc', 'dec'] and d3[1] == d4[1])


def multiply(r, x, y, d3):
    mctr = d3[1]
    if ((d3[0] == 'inc' and r[mctr] >= 0) or
        (d3[0] == 'dec' and r[mctr] <= 0)):
        raise ValueError("Mutliplication will not converge")
    else:
        r[x] += r[y] * r[mctr]
    return r


def parse(r, i, dd, f):
    d0 = dd[i].split(' ')
    if i+2 < len(dd):
        d1 = dd[i+1].split(' ')
        d2 = dd[i+2].split(' ')
    if d0[0] == 'tgl':
        # do toggling stuff
        dd = tgl(i+r[d0[1]], dd)
        i += 1
    elif (i + 2 < len(dd)) and add_check(d0, d1, d2):
        if (i+4 < len(dd)):
            d3 = dd[i+3].split(' ')
            d4 = dd[i+4].split(' ')
            di, r = add(r, d0, d1, d2, d3, d4)
        else:
            di, r = add(r, d0, d1, d2)
        i += di
    else:
        di, r = f[d0[0]](r, *d0[1:])
        i += di
    return (r, i, dd)


def inc(r, a):
    di = 1
    r[a] += 1
    return di, r


def dec(r, a):
    di = 1
    r[a] -= 1
    return di, r


def cpy(r, a, b):
    di = 1
    try:
        a = int(a)
    except:
        a = int(r[a])
    r[b] = a
    return di, r


def jnz(r, x, y):
    di = 1
    try:
        x = int(x)
    except:
        x = r[x]
    if x != 0 and x != '0':
        try:
            y = int(y)
        except:
            y = int(r[y])
        di = y
    return di, r


def tgl(x, dd):
    if x is None:
        raise ValueError('Unexpected None value for x')
    try:
        if x < 0:  # don't want x if it's less than zero
            return dd
        else:
            d = dd[x].split(' ')
    except:  # don't want x if it's larger than the instructions are long
        return dd

    if d[0] == 'cpy':
        dd[x] = ' '.join(['jnz', *d[1:]])
    elif d[0] == 'jnz':
        dd[x] = ' '.join(['cpy', *d[1:]])
    elif d[0] == 'inc':
        dd[x] = ' '.join(['dec', *d[1:]])
    elif d[0] in ['dec', 'tgl']:
        dd[x] = ' '.join(['inc', *d[1:]])
    return dd


def _main(r, data, verbose=False):
    i = 0
    L = len(data)
    f = {'inc': inc, 'dec': dec, 'cpy': cpy, 'jnz': jnz, 'tgl': tgl}
    while i < L:
        if verbose:
            print('\ta = {}, b = {}, c = {}, d = {}'.format(*[r.get(x) for x in 'abcd']))
            input()
            print('\n\tdata[{}] = {}'.format(i, data[i]))
        r, i, data = parse(r, i, data, f)
        # input()
        # print('\n{}'.format(data))
        # print('a: {},\tb: {}'.format(r['a'].value, r['b'].value))
        # print('c: {},\td: {}\n'.format(r['c'].value, r['d'].value))
        # time.sleep(.01)
        # print()
    return r

if __name__ == "__main__":
    data1 = load_data('./input/day23.txt')
    data2 = load_data('./input/day23.txt')
    test_data = ['cpy 2 a', 'tgl a', 'tgl a', 'tgl a',
                 'cpy 1 a', 'dec a', 'dec a']
    test_data2 = ['cpy 12 a', 'cpy a b', 'dec b', 'dec a', 'jnz b -2']

    print('Part 1')
    r1 = {x: None for x in 'abcd'}
    r1['a'] = 7
    r1 = _main(r1, data1)
    print('Answer:')
    print('\ta = {}'.format(r1.get('a')))
    # Answer: 11123

    print('\nPart 2')
    r2 = {x: None for x in 'abcd'}
    r2['a'] = 12
    r2 = _main(r2, data2)
    print('Answer:')
    print('\ta = {}'.format(r2.get('a')))
    # Answer: 479007683
