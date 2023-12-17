from heapq import heappop, heappush
from math import inf
from collections import defaultdict

FILENAME = "d17test"
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


dists = defaultdict(lambda: inf)
heap = [(0, 0, 0, 1, "s"), (0, 0, 0, 1, "e")]  # (total loss, x, y, count to force turn)

while heap:
    # print(heap)
    loss, x, y, movesToForce, direction = heappop(heap)

    if x < 0 or x >= m or y < 0 or y >= n:  # outside of grid
        continue

    if x == m - 1 and y == n - 1:  # at destination
        print(loss)
        break

    if movesToForce > 0:  # Able to continue as normal
        nx, ny = newCoords(x, y, direction)
        if 0 <= nx < m and 0 <= ny < n:
            newLoss = loss + grid[nx][ny]
            if dists[(nx, ny, direction)] >= newLoss:
                dists[(nx, ny, direction)] = newLoss
                heappush(heap, (newLoss, nx, ny, movesToForce - 1, direction))

    # Turns
    for d in turn_dirs[direction]:
        nx, ny = newCoords(x, y, d)
        if 0 <= nx < m and 0 <= ny < n:
            newLoss = loss + grid[nx][ny]
            if dists[(nx, ny, direction)] >= newLoss:
                dists[(nx, ny, direction)] = newLoss
                heappush(heap, (newLoss, nx, ny, 3, direction))