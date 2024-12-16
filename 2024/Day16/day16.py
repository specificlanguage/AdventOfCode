import heapq
from collections import defaultdict, deque
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day16input'
lines = []
boxes = set()

with open(FILEPATH) as f:
    grid = [[e for e in r] for r in f.read().split("\n")]

M, N = len(grid), len(grid[0])
start = ()
end = ()
dirs = [(-1, 0, -90), (1, 0, 90), (0, -1, 180), (0, 1, 0)]

# Find start & end points
for i in range(M):
    for j in range(N):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)

def djikstra(start):
    r, c = start
    parents = {}
    visited = {}
    heap = [(0, r, c, 0, None)]  # Form is going to be (score, curr_r, curr_c, last_dir)
    while heap:
        item = heapq.heappop(heap)
        score, r, c, last_dir, parent = item
        if (r, c) == end:
            return score
        if (r, c, last_dir) in visited and score > visited[(r,c,last_dir)]:  # Visited already with lower score
            continue
        visited[(r,c,last_dir)] = score
        # print(r, c, last_dir, score, parent, len(heap))

        # Keep going in other directions as you can.
        for dr, dc, deg in dirs:
            new_r, new_c = r + dr, c + dc
            new_score = score + 1
            if 0 <= new_r < M and 0 <= new_c < N and grid[new_r][new_c] != "#":
                if deg == last_dir:
                    pass
                elif abs(deg - last_dir) == 90 or abs(deg - last_dir) == 270:
                    new_score += 1000
                else:
                    new_score += 2000

                heapq.heappush(heap, (new_score, new_r, new_c, deg, (r, c)))

print(djikstra(start))



