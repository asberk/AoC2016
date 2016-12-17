# # # #
# Advent of Code 2016
# Day 17
# By Aaron Berk
# Puzzle Input: pxxbnzuo
# # # #

from collections import deque
from hashlib import md5


# pz is the puzzle input, path is the path so far
def md5hash(pz, path):
    return md5((pz+path).encode('utf-8')).hexdigest()


class Vertex:
    pz = 'pxxbnzuo'

    def __init__(self, x=None, y=None, vn=None, vp=None):
        self.x = x
        self.y = y
        self.P = (x, y)
        # self.valid = self.isValid()
        self.explored = False
        if vn is None:
            vn = 1e6
        self.visitNumber = vn
        if vp is None:
            vp = ''
        self.visitPath = vp
        self.neighbours = self.getNeighbours()

    def inBounds(self, P=None):
        if P is None:
            x = self.x
            y = self.y
        else:
            x = P[0]
            y = P[1]
        x_in_rooms = x >= 0 and x <= 3
        y_in_rooms = y >= 0 and y <= 3
        return x_in_rooms and y_in_rooms

    def getNeighbours(self):
        nei = {'U': (self.x, self.y-1),
               'D': (self.x, self.y+1),
               'L': (self.x-1, self.y),
               'R': (self.x+1, self.y)}

        # runs in order U D L R
        ph = md5hash(self.pz, self.visitPath)[:4]
        keys = 'UDLR'
        good_letters = 'bcdef'
        path_hash = {}
        for i, j in enumerate(keys):
            path_hash[j] = ph[i] in good_letters

        goodNeighbours = {}
        for p, P in nei.items():
            if self.inBounds(P) and path_hash[p]:
                goodNeighbours[p] = P
        return goodNeighbours

    def nei(self):
        self.neighbours = self.getNeighbours()


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

    def ShortestPath(self, v0, v1):
        V = self.V
        if v0 not in V.keys():
            print('\tStarting vertex is invalid.')
            return
        Q = deque()
        Q.append(Vertex(v0[0], v0[1], vn=0))
        while len(Q) > 0:  # we'll break from inside
            v = Q.popleft()
            if v.P == v1:
                vn = v.visitNumber
                print('\tVertex {} found after {} steps.'.format(v.P, vn))
                return v.visitPath
            for p, P in v.neighbours.items():
                n = Vertex(P[0], P[1], v.visitNumber+1, v.visitPath+p)
                Q.append(n)
        print('\tVertex not found from traversal.')
        return

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

    def LongestPath(self, v0, v1):
        # Longest Path So Far
        LPSF = ''
        LPLSF = len(LPSF)
        V = self.V
        if v0 not in V.keys():
            print('\tStarting vertex is invalid.')
            return
        Q = deque()
        Q.append(Vertex(v0[0], v0[1], vn=0))
        while not all(q.P == v1 for q in Q) and len(Q) > 0:
            v = Q.popleft()
            if v.P == v1:
                if v.visitNumber > LPLSF:
                    LPSF = v.visitPath
                    LPLSF = v.visitNumber
                Q.append(v)
            else:
                v.nei()  # make sure neighbours are up to date
                for p, P in v.neighbours.items():
                    n = Vertex(P[0], P[1], v.visitNumber+1, v.visitPath+p)
                    n.nei()  # make sure neighbour's neighbours are up to date
                    Q.appendleft(n)
        print('\tLongest path length: {}.'.format(LPLSF))
        return LPSF

    def reset(self, visitNumber=None):
        if visitNumber is None:
            vn = self.unvisited
        else:
            vn = visitNumber
        for v in self.V.values():
            v.explored = False
            v.visitNumber = vn
        return


if __name__ == "__main__":
    makeimages = 0
    pz = 'pxxbnzuo'
    X = 4
    Y = 4
    G = Graph(X, Y)
    print('Part 1')
    shortestPath = G.ShortestPath((0, 0), (3, 3))
    print('\tShortest path is:')
    print('\t\t{}'.format(shortestPath))

    print('Part 2')
    G2 = Graph(X, Y)
    longestPath = G2.LongestPath((0, 0), (3, 3))
    print('\tLongest path is:')
    print('\t\t{}'.format(longestPath))
