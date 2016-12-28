# # # # # #
# Advent of Code 2016
# Day 24
# By Aaron Berk
#
# Notes: in general, this problem is NP-hard, so we'll just have to run it
#        brute force with what speed-ups we can muster.
# # # # # #

from load_data import load_data
from collections import deque
from itertools import permutations


class Vertex:
    def __init__(self, x=None, y=None, kind=None, visnum=None):
        self.x = x
        self.y = y
        self.P = (x, y)
        self.explored = False
        if visnum is None:
            visnum = 1e6
        self.visitNumber = visnum
        if kind is None:
            kind = ''
        self.kind = kind
        self.neighbours = self.getNeighbourAddresses()

    def inBounds(self, B=None, P=None):
        if P is None:
            x = self.x
            y = self.y
        else:
            x = P[0]
            y = P[1]
        if B is None:
            x_in_rooms = x >= 0
            y_in_rooms = y >= 0
        else:
            x_in_rooms = x >= 0 and x < B[0]
            y_in_rooms = y >= 0 and y < B[1]
        return x_in_rooms and y_in_rooms

    def getNeighbourAddresses(self, B=None):
        nei = {'U': (self.x, self.y-1),
               'D': (self.x, self.y-1),
               'L': (self.x-1, self.y),
               'R': (self.x+1, self.y)}
        goodNeighbours = {}
        for p, P in nei.items():
            if self.inBounds(B=B):
                goodNeighbours[p] = P
        return goodNeighbours


class Graph:
    unvisited = 1e6

    def __init__(self, data):
        self.data = data
        self.X = len(data[0])
        self.Y = len(data)
        self.V = {}
        for x in range(self.X):
            for y in range(self.Y):
                self.V[(x, y)] = Vertex(x, y, data[y][x])
        self.updateAllGraphNeighbours()
        return

    def updateAllGraphNeighbours(self):
        for x in range(self.X):
            for y in range(self.Y):
                self.updateNeighbours((x, y))
        return

    def updateNeighbours(self, Q):
        x = Q[0]
        y = Q[1]
        Q = self.V[Q]
        nei = {'U': (x, y-1), 'D': (x, y+1),
               'L': (x-1, y), 'R': (x+1, y)}
        Q.neighbours = {p: P for p, P in nei.items()
                        if (Q.inBounds(B=(self.X, self.Y), P=P) and
                            self.V[P].kind != '#')}
        return

    def nei(self, v):
        x = v.x
        y = v.y
        nei = {'U': (x, y-1), 'D': (x, y-1),
               'L': (x-1, y), 'R': (x+1, y)}
        return [Vertex(P[0], P[1], kind=self.data[P[1]][P[0]],
                       visnum=v.visitNumber+1)
                for p, P in nei.items() if self.data[P[1]][P[0]] != '#']

    def shortestPath(self, v0, v1):
        V = self.V
        if v0 not in V.keys():
            print('\tStarting vertex is invalid.')
            return
        Q = deque()
        Q.append(V[v0])
        V[v0].explored = True
        V[v0].visitNumber = 0
        while len(Q) > 0:
            v = Q.popleft()
            if v.P == v1:
                vn = v.visitNumber
                # print('\tVertex {} found after {} steps.'.format(v.P, vn))
                return v.visitNumber
            for ell, address in v.neighbours.items():
                n = V[address]
                if n.kind != '#' and not n.explored:
                    n.explored = True
                    n.visitNumber = v.visitNumber + 1
                    Q.append(n)
        print('\tVertex not found from traversal.')
        return

    def reset(self):
        for P, v in self.V.items():
            v.explored = False
            v.visitNumber = self.unvisited
        return


def parse(data):
    G = Graph(data)
    nums = {str(j): None for j in range(8)}
    for num, val in nums.items():
        for y, row in enumerate(data):
            try:
                x = row.index(num)
                nums[num] = (x, y)
            except:
                continue
    return G, nums


def shortestMultiPath(G, pts, perms):
    shortestPath = 1e10
    for perm in perms:
        pathLength = 0
        # print('\tFinding shortest path for {}.'.format(perm))
        for j in range(1, len(perm)):
            v0 = pts[perm[j-1]]
            v1 = pts[perm[j]]
            # print('\tPath from {} to {}.'.format(v0, v1))
            pathLength += G.shortestPath(v0, v1)
            G.reset()
            if pathLength > shortestPath:
                break
        if pathLength < shortestPath:
            shortestPath = pathLength
        print('\tShortest path so far: {}'.format(shortestPath), end='\r')
    return shortestPath


if __name__ == "__main__":
    data = load_data('./input/day24.txt')

    perms = permutations([str(j) for j in range(1, 8)])
    perms1 = [tuple(['0', *perm]) for perm in perms]
    perms = permutations([str(j) for j in range(1, 8)])
    perms2 = [('0', *perm, '0') for perm in perms]
    G, nums = parse(data)
    shortestPath1 = shortestMultiPath(G, nums, perms1)

    print('\nPart 1')
    print('\t{}'.format(shortestPath1))
    # Answer is 442

    G.reset()
    shortestPath2 = shortestMultiPath(G, nums, perms2)
    print('\nPart 2')
    print('\t{}'.format(shortestPath2))
