# From https://github.com/michaeljgallagher/Advent-of-Code/blob/master/2023/17.py

from collections import defaultdict
from heapq import heappop, heappush
from math import inf

with open("d17input", "r") as file:
    data = file.read().strip()

GRID = data.split("\n")


def dijkstra(grid, lo, hi):
    n, m = len(grid), len(grid[0])
    dists = defaultdict(lambda: inf)

    heap = [(0, (0, 0, (0, 1))), (0, (0, 0, (1, 0)))] # (0, 1) with direction south, (1, 0) with direction east

    while heap:
        cost, (i, j, d) = heappop(heap)
        if (i, j) == (n - 1, m - 1):  # At destination
            return cost
        if cost > dists[i, j, d]:  # Check if we have a better cost, then don't proceed with this
            continue
        di, dj = d
        for ndi, ndj in ((-dj, di), (dj, -di)):  # Turn if necessary
            ncost = cost
            for dist in range(1, hi + 1): # Go in x direction for dist amount
                ni, nj = i + ndi * dist, j + ndj * dist
                if 0 <= ni < n and 0 <= nj < m:  # Only do so if in limits
                    ncost += int(grid[ni][nj]) # Add cost of next node
                    if dist < lo: # If our distance is not enough
                        continue
                    k = (ni, nj, (ndi, ndj))
                    if ncost < dists[k]:  # if our cost is better than existing, then continue on!
                        dists[k] = ncost
                        heappush(heap, (ncost, k))
    return -1

print(dijkstra(GRID, 1, 3))
print(dijkstra(GRID, 4, 10))