from load_data import load_data
from collections import deque


class Node:
    def __init__(self, x=None, y=None, size=None, used=None):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = self.size - self.used
        self.pctfull = self.used / self.size
        self.viable = []

    def _viable(self, N):
        if self.used > 0:
            if (self.x == N.x and self.y == N.y):
                return
            elif self.used < N.avail:
                self.viable.append(N)
                return
            return
        return


class Grid:
    def __init__(self, maxX, maxY):
        self.X = maxX
        self.Y = maxY
        self.nodes = {}
        for j in range(maxX):
            self.nodes[j] = {}
            for k in range(maxY):
                self.nodes[j][k] = None
        return

    def get(self, x, y):
        return self.nodes[x][y]

    def addNode(self, x=None, y=None, size=None, used=None):
        self.nodes[x][y] = Node(x, y, size, used)
        return

    def loadGrid(self, data):
        for d in data:
            self.addNode(*parse(d))
        return

    def viable(self):
        for x1 in range(self.X):
            for y1 in range(self.Y):
                if self.nodes[x1][y1].used == 0:
                    continue
                for x2 in range(self.X):
                    for y2 in range(self.Y):
                        self.nodes[x1][y1]._viable(self.nodes[x2][y2])


def parse(d):
    d = d.split()
    xy = d[0].split('-')
    x = int(xy[1][1:])
    y = int(xy[2][1:])
    size = int(d[1][:-1])  # in Terabytes
    used = int(d[2][:-1])
    return (x, y, size, used)

if __name__ == "__main__":
    data = load_data('./input/day22.txt')
    nodes = [Node(*parse(d)) for d in data[2:]]
    viable_pairs = deque()
    maxX = 0
    maxY = 0
    for n in nodes:
        maxX = max(maxX, n.x)  # for part 2
        maxY = max(maxY, n.y)  # for part 2
        for m in nodes:
            if n.used == 0 or (n.x == m.x and n.y == m.y):
                continue
            else:
                if n.used < m.avail:
                    viable_pairs.append((n, m))
    print('Part 1')
    print(len(viable_pairs))

    print('Part 2')
    gd = Grid(maxX+1, maxY+1)  # counts from 0
    gd.loadGrid(data[2:])
