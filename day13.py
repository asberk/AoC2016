# # # #
# Advent of Code
# Day 13
# Puzzle input: 1352
# Looking to reach: (31, 39)
# By: Aaron Berk
# Options: Turn on makeimages for a visualization of the results
# Answer for (a): 90
# Answer for (b): 135
from collections import deque
import matplotlib.pyplot as plt


class Vertex:

    fav = 1352

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.P = (x, y)
        self.valid = self.isValid()
        self.explored = False
        self.visitNumber = 1e6
        self.neighbours = self.getNeighbours()

    def isValid(self, P=None):
        if P is None:
            x = self.x
            y = self.y
        else:
            x = P[0]
            y = P[1]
        return x >= 0 and y >= 0 and self.validHash(P)

    def coordHash(self, x, y):
        return (x+y)**2 + 3*x + y

    def validHash(self, P=None):
        if P is None:
            x = self.x
            y = self.y
        else:
            x = P[0]
            y = P[1]
        loc_hash = self.coordHash(x, y) + self.fav
        bitsum = sum(1 for j in bin(loc_hash) if j == '1')
        return bitsum % 2 == 0

    def getNeighbours(self):
        l = (self.x - 1, self.y)
        r = (self.x + 1, self.y)
        u = (self.x, self.y - 1)
        d = (self.x, self.y + 1)
        goodNeighbours = []
        for v in [l, r, u, d]:
            if self.isValid(v):
                goodNeighbours.append(v)
        return goodNeighbours


class Graph:

    unvisited = 1e6

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.V = {}
        # E = []
        for x in range(X):
            for y in range(Y):
                self.V[(x, y)] = Vertex(x, y)
                # I don't think I need the edge list right now.
                # for nei in V[(x, y)].neighbours:
                #     E.append(((x, y), nei))

    def BFS(self, v0, v1):
        """
        BFS(self, v0, v1) performs a breadth-first search to look for a path
        from vertex v0 at (x0, y0) to vertex v1 at (x1, y1).
        """
        V = self.V
        if v0 not in V.keys() or v1 not in V.keys():
            print('one of the vertices v0, v1 is invalid')
            return None  # => there is no path
        elif V[v1].explored:
            print('Found v1. Visited after '
                  '{} steps.'.format(V[v1].visitNumber))
        Q = deque()
        Q.append(V[v0])
        V[v0].explored = True
        V[v0].visitNumber = 0
        while len(Q) > 0:
            v = Q.popleft()
            if v.P == v1:
                print('Found v1. Visited after '
                      '{} steps.'.format(v.visitNumber))
                return v
            for address in v.neighbours:
                if address[0] >= self.X or address[1] >= self.Y:
                    continue
                n = V[address]
                if not n.explored:
                    n.explored = True
                    n.visitNumber = v.visitNumber + 1
                    Q.append(n)
        print('vertex not found from traversal')
        return

    def DFS(self, v0, max_steps=50):
        """
        DFS(self, max_steps) performs a depth-first search to to look for all
        possible coords that can be reached in no more than max_steps steps.
        """
        V = self.V
        if v0 not in V.keys():
            print('Starting vertex is invalid.')
            return  # there is no path
        visitedVertices = deque()
        Q = deque()
        visitedVertices.append(v0)
        Q.append(V[v0])
        V[v0].explored = True
        V[v0].visitNumber = 0
        while len(Q) > 0:
            v = Q.popleft()
            if v.visitNumber == 50:
                continue
            for address in v.neighbours:
                if address[0] >= self.X or address[1] >= self.Y:
                    continue  # don't include neighbours that lie outside G
                n = V[address]
                if (not n.explored) and n.visitNumber <= 50:
                    n.explored = True
                    n.visitNumber = v.visitNumber + 1
                    visitedVertices.append(address)
                    Q.append(n)
        return visitedVertices

    def reset(self, visitNumber=None):
        if visitNumber is None:
            vn = self.unvisited
        else:
            vn = visitNumber
        for v in self.V.values():
            v.explored = False
            v.visitNumber = vn
        return

    def makeImage(self):
        output = [[1 if self.V[(x, y)].isValid() else 0
                   for x in range(X)]
                  for y in range(Y)]
        for y, row in enumerate(output):
            for x, elem in enumerate(row):
                if self.V[(x, y)].explored:
                    output[y][x] = .3
        plt.matshow(output, cmap='gray')
        plt.show()
        return

if __name__ == "__main__":
    makeimages = 0
    X = 43
    Y = 50
    G = Graph(X, Y)
    v1 = G.BFS((1, 1), (31, 39))
    if makeimages:
        G.makeImage()
    G.reset(0)
    visited = G.DFS((1, 1))
    print('Number of vertices visited in at most '
          '50 steps is {}'.format(len(visited)))
    if makeimages:
        G.makeImage()
