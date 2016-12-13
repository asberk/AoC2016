# # # #
# Advent of Code
# Day 12
# Puzzle input: 1352
# Looking to reach: (31, 39)
# By: Aaron Berk
#
# Descripton: a more bare-bones way of doing day12.py, since I couldn't figure
# out what was going on with day12.py. This has since been figured out. They
# are likely to take about the same amount of time.
# Answer for part (a): 318077
# Answer for part (b): 9227731
# # # #

from load_data import load_data


def get_idx(letter):
    if letter == 'a':
        return 0
    elif letter == 'b':
        return 1
    elif letter == 'c':
        return 2
    elif letter == 'd':
        return 3
    else:
        raise Exception('expected letters a, b, c or d')


index = {'a': 0, 'b': 1, 'c': 2, 'd': 3}


def _main(data, verbose=0):
    abcd = [None]*4
    i = 0
    L = len(data)
    while i < L:
        d = data[i].split(' ')
        if d[0] == 'cpy':
            x = d[1]
            if x in ['a', 'b', 'c', 'd']:
                x_idx = index.get(d[1])
                y_idx = index.get(d[-1])
                abcd[y_idx] = abcd[x_idx]
                i += 1
            else:
                y_idx = index.get(d[-1])
                abcd[y_idx] = int(d[1])
                i += 1
        elif d[0] == 'jnz':
            if d[1] in ['a', 'b', 'c', 'd']:
                x = abcd[index.get(d[1])]
            else:
                x = int(d[1])
            if x == 0 or x is None:
                i += 1
            else:
                i += int(d[-1])
        elif d[0] == 'inc':
            abcd[index.get(d[1])] += 1
            i += 1
        elif d[0] == 'dec':
            abcd[index.get(d[1])] -= 1
            i += 1
        else:
            print('command not recognized')
        if verbose and abcd[1] == 0:
            print('a = {}'.format(abcd[0]))
    return abcd

if __name__ == "__main__":
    data = load_data('./input/day12.txt')
    test_data = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']
    abcd = _main(data)
    print('Done!')
    print('a = {}'.format(abcd[0]))
