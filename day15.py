from load_data import load_data


class Disc:
    def __init__(self, location, num_posns, t0, posn0):
        self.location = location
        self.num_posns = num_posns
        self.t0 = t0
        self.posn0 = posn0

    def activation(self, N):
        x = (self.location + self.posn0 - self.t0 + N) % self.num_posns
        return x == 0


def _parse(d):
    d = d.split(' ')
    disc_number = int(d[1][1:])
    num_posns = int(d[3])
    t0 = int(d[6][d[6].index('=')+1:-1])
    posn0 = int(d[-1][:-1])
    return(disc_number, num_posns, t0, posn0)


if __name__ == "__main__":
    data = load_data('./input/day15.txt')

    print('Part 1')
    discs = [Disc(*_parse(d)) for d in data]
    N = 0
    while not all(d.activation(N) for d in discs):
        N += 1
    print('\tFirst N is: {}'.format(N))

    print('\nPart 2')
    discs2 = [Disc(*_parse(d)) for d in data]
    discs2.append(Disc(discs2[-1].location+1, 11, 0, 0))
    N2 = 0
    while not all(d.activation(N2) for d in discs2):
        N2 += 1
    print('\tFirst N is: {}'.format(N2))
