from collections import deque
# 1 2 3 4 5 6 7

# White Elephant Winner
def wew(pz, PRINT_OUTPUT=0):
    elves = list(range(1, pz+1))
    if PRINT_OUTPUT:
        print('\t{}'.format(elves))

    while len(elves) > 1:
        wrap = (len(elves) % 2 == 1)
        elves = elves[::2]
        if wrap:
            elves.pop(0)
        if PRINT_OUTPUT:
            print('\t{}'.format(elves))
    return elves[0]


def wew2(pz, PRINT_OUTPUT=0):
    elves = list(range(1, pz+1))
    idx = 0
    L = len(elves)
    while L > 1:
        rm = (idx + L//2) % L
        if idx < 10 and PRINT_OUTPUT:
            print('\t(at, taking): ({}, {})'.format(idx, rm))
        del elves[rm]
        if rm > idx:
            idx = (idx + 1) % L
        L = len(elves)
    return elves[0]


class Node:
    def __init__(self, id):
        self.id = id
        self.nxt = None
        self.prv = None

    def delete(self):
        self.prv.nxt = self.nxt
        self.nxt.prv = self.prv


def solve(n):
    l = list(map(Node, range(n)))
    for j in range(n):
        l[j].nxt = l[(j+1)%n]
        l[j].prv = l[(j-1)%n]

    start = l[0]
    mid = l[n//2]

    for j in range(n-1):
        mid.delete()
        mid = mid.nxt
        if (n-j) % 2 == 1:
            mid = mid.nxt
        start = start.nxt
    return start.id + 1


if __name__ == "__main__":
    pz = 3014603

    print('Test data 1')
    wew(5, True)  # 3
    wew(7, True)  # 7
    wew(8, True)  # 1
    wew(9, True)  # 3

    print('\nPart 1')
    last_elf = wew(pz)
    print('\tLast elf remaining is number {}.'.format(last_elf))
    # Answer: 1834903

    print('Test data 2')
    for j in range(1, 10):
        wj = wew2(j)
        print('({2:05d}, {0}, {1})'.format(j, wj, int(bin(wj)[2:])))

    print('\nPart 2')
    new_last_elf = solve(pz)
    print('\tLast elf remaining is number {}.'.format(new_last_elf))
    # Answer: 1420280
