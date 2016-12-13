# # # #
# Advent of Code
# Day 12
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
import time


class Register():
    def __init__(self, value=None):
        self.value = value

    def set(self, value):
        self.value = value
        return

    def get(self):
        return self.value

    def inc(self):
        self.value += 1
        return

    def dec(self):
        self.value -= 1
        return

    def cpy(self, a):
        if isinstance(a, Register):
            self.set(a.get())
        elif isinstance(a, int) or isinstance(a, float):
            self.set(a)
        else:
            raise ValueError('expected a to be int, float or Register')
        return


def parse(i, d, r):
    d = d.split(' ')
    if d[0] == 'cpy':
        val = r.get(d[1])
        if not val:
            val = int(d[1])
        r[d[-1]].cpy(val)
        i += 1
    elif d[0] == 'jnz':
        try:
            val = int(d[1])
        except:
            val = r[d[1]].get()
        if val == 0 or val is None:
            i += 1
        else:
            i += int(d[2])
    elif d[0] == 'inc':
        r[d[1]].inc()
        i += 1
    elif d[0] == 'dec':
        r[d[1]].dec()
        i += 1
    return (i, r)


def _main(data):
    verbose = 0
    r = {'a': Register(), 'b': Register(),
         'c': Register(), 'd': Register()}

    i = 0
    L = len(data)
    while i < L:
        i, r = parse(i, data[i], r)
        if verbose and r['b'].value == 0:
            print(r['a'].value)
        # print(data[i])
        # print('a: {},\tb: {}'.format(r['a'].value, r['b'].value))
        # print('c: {},\td: {}\n'.format(r['c'].value, r['d'].value))
        # time.sleep(.01)
        # print()
    return r

if __name__ == "__main__":
    data = load_data('./input/day12.txt')
    test_data = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']

    r = _main(data)
    print(r['a'].get())


# # # Answer for part (a): 318077
# # # Answer for part (b): 9227731
