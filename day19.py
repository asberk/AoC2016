# # # # # #
# Advent of Code 2016
# Day 19
# By Aaron Berk
# # # # # #

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


# second way of solving Josephus's problem
def wew2(n):
    b = bin(n)[2:]
    return int(b[1:] + b[0], 2)


class Elf:
    def __init__(self, id):
        self.id = id
        self.nxt = None
        self.prv = None

    def delete(self):
        self.prv.nxt = self.nxt
        self.nxt.prv = self.prv


def solve(n):
    # get a new n-tuple of elves
    l = [Elf(j) for j in range(n)]

    # set neighbours
    for j in range(n):
        l[j].nxt = l[(j+1) % n]
        l[j].prv = l[(j-1) % n]

    # starting elf and mid elf
    start = l[0]
    mid = l[n//2]

    # loop through elves
    for j in range(n-1):
        # kill the start elf's middle elf.
        mid.delete()
        # the pattern for which middle elf is next
        # alternates as:
        #    +2, +1, +2, +1, ...
        # or +1, +2, +1, +2, ...
        # so just figure out which:
        mid = mid.nxt
        if (n-j) % 2 == 1:
            mid = mid.nxt
        # now it's the next elf's turn to kill
        start = start.nxt
    # there's one elf remaining after n-1 turns;
    # return its name, which is its location id + 1
    return start.id + 1


if __name__ == "__main__":
    pz = 3014603

    print('\nPart 1')
    last_elf = wew(pz)
    same_last_elf = wew2(pz)
    print('\tLast elf remaining is number {}.'.format(last_elf))
    print('\tThe clever way still gets the same '
          'answer: {}.'.format(same_last_elf))
    # Answer: 1834903

    print('\nPart 2')
    new_last_elf = solve(pz)
    print('\tLast elf remaining is number {}.'.format(new_last_elf))
    # Answer: 1420280
