from load_data import load_data
from copy import copy


def swap(s, kind, X, Y):
    if kind == 'position':
        return swap_position(s, X, Y)
    elif kind == 'letter':
        return swap_letter(s, X, Y)
    else:
        raise ValueError('expected one of "position" or "letter" for swap')


def swap_position(s, X, Y):
    t = copy(s)
    t[X] = s[Y]
    t[Y] = s[X]
    return t


def swap_letter(s, X, Y):
    a = s.index(X)
    b = s.index(Y)
    t = copy(s)
    t[b] = X
    t[a] = Y
    return t


def rotate(s, kind, X):
    if kind == 'letter':
        return rotate_by_letter(s, X)
    elif kind in ['left', 'right']:
        return rotate_lr(s, kind, X)
    else:
        raise ValueError('expected one of "letter", "left", "right" for rotate')


def rotate_by_letter(s, X):
    S = len(s)
    j = s.index(X)
    n = j+1
    if j >= 4:
        n += 1
    return [s[(k-n) % S] for k in range(S)]


def rotate_lr(s, kind, X):
    S = len(s)
    if kind == 'left':
        n = X
    elif kind == 'right':
        n = -X
    else:
        raise ValueError('expected one of "left", "right" for rotate_lr')
    return [s[(k+n) % S] for k in range(S)]


def reverse(s, X, Y):
    return s[:X] + s[Y:X:-1] + [s[X]] + s[Y+1:]


def move(s, X, Y):
    t = copy(s)
    a = t.pop(X)
    t.insert(Y, a)
    return t


def parse(d):
    d = d.split(' ')
    if d[0] == 'rotate':
        if d[1] in ['left', 'right']:
            return (d[0], d[1], int(d[2]))
        else:
            return (d[0], 'letter', d[-1])
    elif d[0] == 'swap':
        if d[1] == 'position':
            return (d[0], d[1], int(d[2]), int(d[-1]))
        else:  # letter
            return (d[0], d[1], d[2], d[-1])
    elif d[0] == 'move':
        return (d[0], int(d[2]), int(d[-1]))
    elif d[0] == 'reverse':
        return (d[0], int(d[2]), int(d[-1]))
    else:
        raise ValueError('did not recognize d[0]')


def invrotate_by_letter(s, X):
    for j in range(len(s)):
        t = rotate_lr(s, 'left', j)
        if s == rotate_by_letter(t, X):
            return t
    raise Exception('No inverse rotation by letter found')


def invparse(d):
    d = d.split(' ')
    if d[0] == 'rotate':
        if d[1] == 'left':
            return (d[0], 'right', int(d[2]))
        elif d[1] == 'right':
            return (d[0], 'left', int(d[2]))
        else:
            return ('invrotate_by_letter', d[-1])
    elif d[0] == 'swap':
        if d[1] == 'position':
            return (d[0], d[1], int(d[-1]), int(d[2]))
        else:  # letter
            return (d[0], d[1], d[-1], d[2])
    elif d[0] == 'move':
        return (d[0], int(d[-1]), int(d[2]))
    elif d[0] == 'reverse':
        return (d[0], int(d[2]), int(d[-1]))
    else:
        raise ValueError('did not recognize d[0]')
    return

if __name__ == "__main__":
    data = load_data('./input/day21.txt')
    f = {'rotate': rotate, 'swap': swap, 'move': move, 'reverse': reverse,
         'invrotate_by_letter': invrotate_by_letter}

    print('Part 1')
    s1 = list('abcdefgh')
    for d in data:
        d = parse(d)
        # func = f[d[0]]
        s1 = f[d[0]](s1, *d[1:])
    print(''.join(s1))
    # Answer: hcdefbag

    print('\nPart 2')
    s2 = list('fbgdceah')
    for d in data[::-1]:
        d = invparse(d)
        s2 = f[d[0]](s2, *d[1:])
    print(''.join(s2))
    # Answer: fbhaegdc
