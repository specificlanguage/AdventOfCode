from heapq import heappop, heappush
from math import inf
from collections import defaultdict

FILENAME = "d17input"
PART = 1

grid = []

for line in open(FILENAME):
    grid.append([int(c) for c in line.strip()])

m, n = len(grid), len(grid[0])

turn_dirs = {"n": ["w", "e"], "s": ["w", "e"], "w": ["n", "s"], "e": ["n", "s"]}
diffs = {"n": (-1, 0), "s": (1, 0), "w": (0, -1), "e": (0, 1)}
visit = {"n": "^", "s": "v", "w": "<", "e": ">"}

def newCoords(x, y, d):
    return x + diffs[d][0], y + diffs[d][1]

heap = [(0, 0, 0, 1, "s"), (0, 0, 0, 1, "e")]  # (total loss, x, y, count to force turn)

def dijkstra(grid, low, high):
    m, n = len(grid), len(grid[0])
    dists = defaultdict(lambda: inf)

    heap = [(0, 0, 0, 3, "s"), (0, 0, 0, 3, "e")]  # loss, x, y, movesToForce, direction
    while heap:
        cost, i, j, mtf, d = heappop(heap)

        if (i, j) == (m-1, n-1):
            return cost
        if cost > dists[i, j, mtf, d]:
            continue

        # print(cost, i, j, mtf, d)

        if mtf > low: # It turns out we can't do more than x in a row, rather than going down to low.
            ni, nj = newCoords(i, j, d)
            if 0 <= ni < m and 0 <= nj < n:
                newLoss = cost + grid[ni][nj]
                if newLoss < dists[i, j, mtf-1, d]:
                    dists[i, j, mtf-1, d] = newLoss
                    heappush(heap, (newLoss, ni, nj, mtf - 1, d))

        for nd in turn_dirs[d]:
            ni, nj = newCoords(i, j, nd)
            if 0 <= ni < m and 0 <= nj < n:
                newLoss = cost + grid[ni][nj]
                if newLoss < dists[i, j, high, nd]:
                    dists[i, j, high, nd] = newLoss
                    heappush(heap, (newLoss, ni, nj, high, nd))

    return -1

# PART 1
print(dijkstra(grid, 1, 3))

# PART 2
print(dijkstra(grid, 4, 10))