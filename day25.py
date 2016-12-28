from load_data import load_data
from collections import deque


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


def out(r, x=None):
    if x is None:
        raise ValueError('Unexpected None value for x')
    try:
        return int(x)
    except:
        return 1, r, r[x]


def parse(r, i, dd, f, outstream=[]):
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
    elif d0[0] == 'out':
        di, r, output = f[d0[0]](r, *d0[1:])
        i += di
        outstream.append(output)
    else:
        di, r = f[d0[0]](r, *d0[1:])
        i += di
    return (r, i, dd, outstream)


def outstreamcheck(x):
    return (x is None or len(x) == 1 or
            all((x[j-1] == 0 and x[j] == 1) or
                (x[j-1] == 1 and x[j] == 0)
                for j in range(1, len(x))))


def main(r, data, verbose=False):
    THRESH = 1000
    i = 0
    L = len(data)
    f = {'inc': inc, 'dec': dec, 'cpy': cpy, 'jnz': jnz,
             'tgl': tgl, 'out': out}
    outstream = deque()
    while i < L and outstreamcheck(outstream) and len(outstream) < THRESH:
        if verbose:
            print('\ta = {}, b = {}, c = {}, d = {}'.format(*[r.get(x) for x in 'abcd']))
            input()
            print('\n\tdata[{}] = {}'.format(i, data[i]))
        r, i, data, outstream = parse(r, i, data, f, outstream)
    return r, outstream


if __name__ == "__main__":
    data = load_data('./input/day25.txt')

    a0 = 0
    print('Part 1')
    while a0 < 1000:
        r1 = {x: None for x in 'abcd'}
        r1['a'] = a0
        print(a0)
        r1, os1 = main(r1, data)
        if len(os1) > 500:
            print('\tAnswer: {}.'.format(a0))
            break
        a0 += 1
    # Answer: 198
