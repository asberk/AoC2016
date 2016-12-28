# # # # # #
# Advent of Code 2016
# Day 1 Part 2
# By Aaron Berk
#
# Notes: didn't realize there was a part 2 for day 1 until day 27! :P
# # # # # #

from load_data import load_data
from collections import deque
from copy import copy
import numpy as np


def rotateElf(rot, dirn):
    if rot == 'R':
        sgn = 1
    elif rot == 'L':
        sgn = -1
    else:
        raise ValueError('rotateElf error: rotation not recognized')
    return ((dirn + sgn) % 4)


def moveElf(dirn, dist, curpos):
    if dirn == 0:  # North
        return (curpos[0], curpos[1] + dist)
    elif dirn == 1:  # East
        return (curpos[0] + dist, curpos[1])
    elif dirn == 2:  # South
        return (curpos[0], curpos[1] - dist)
    elif dirn == 3:  # West
        return (curpos[0] - dist, curpos[1])
    else:
        raise ValueError('moveElf error: direction not recognized')


def updateVisited(p0, p1, seen, verbose=False):
    x0 = p0[0]
    y0 = p0[1]
    x1 = p1[0]
    y1 = p1[1]
    dups = None
    if x0 == x1 and y0 == y1:
        return
    elif x0 == x1:  # same x coords
        if verbose:
            print('same x coords')
            print('{} -> {}'.format(y0, y1))
        sgn = np.sign(y1-y0)
        for y in range(sgn + y0, sgn + y1, sgn):
            pp = (x0, y)
            if verbose:
                print(pp)
            seen.append(pp)
            if seen.count(pp) > 1:
                if verbose:
                    print()
                return (seen, pp)
            else:
                continue
        if verbose:
            print()
        return (seen, dups)
    elif y0 == y1:
        if verbose:
            print('same y coords')
            print('{} -> {}'.format(x0, x1))
        sgn = np.sign(x1-x0)
        for x in range(sgn + x0, sgn + x1, sgn):
            pp = (x, y0)
            if verbose:
                print(pp)
            seen.append(pp)
            if seen.count(pp) > 1:
                if verbose:
                    print()
                return (seen, pp)
            else:
                continue
        if verbose:
            print()
        return (seen, dups)
    else:
        raise Exception('updateVisited error: (x0, y0) == (x1, y1).')
    return


def updateElf(dd, dirn, curpos, vis, verbose=False):
    rot = dd[0]
    dist = int(dd[1:])
    new_dirn = rotateElf(rot, dirn)
    newpos = moveElf(new_dirn, dist, curpos)
    if verbose:
        print('positions:')
        print(curpos)
        print(newpos)
        print()
    newvis, dups = updateVisited(curpos, newpos, vis, verbose)
    return (new_dirn, newpos, newvis, dups)


if __name__ == "__main__":
    data = load_data('./input/day01.txt')
    data = data[0].split(', ')

    direction = 0  # North
    position = (0, 0)  # starting position is origin
    visited = deque()  # deque of visited positions
    visited.append(position)

    for d in data:
        direction, position, visited, dups = updateElf(d, direction,
                                                       position, visited)
        if dups is not None:
            print('Part 2')
            print('\tPoint {} gives distance {}.'.format(dups, np.linalg.norm(dups, 1)))
            break
