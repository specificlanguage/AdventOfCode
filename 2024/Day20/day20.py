# For a much cleaner solution, just use part 2's solution, and change the manhattan check to 2 instead of 20.

import heapq
from collections import defaultdict, deque, Counter
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day20input'
lines = []

with open(FILEPATH) as f:
    grid = [[e for e in r] for r in f.read().split("\n")]

M, N = len(grid), len(grid[0])
start = ()
end = ()
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'E':
            end = (r, c)

print(end)

def isValidCheat(r, c, dr, dc):
    nr, nc = r + 2 * dr, c + 2 * dc
    if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] != '#':
        return True, nr, nc
    return False, r, c

times = []
cache = {}

def BFS(start, cheats=1):
    if (start, cheats) in cache:
        # print("cached result")
        return cache[(start, cheats)]
    start_r, start_c = start
    queue = deque([(start_r, start_c, 0)]) # Row, col, curr score, cheats left
    visited = set()

    while queue:
        r, c, time = queue.popleft()
        if (r, c) == end:
            cache[(start, cheats)] = time
            return time
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in dirs:
            if 0 <= r + dr < M and 0 <= c + dc < N:

                if grid[r + dr][c + dc] == '#' and cheats > 0:
                    validCheat, nr, nc = isValidCheat(r, c, dr, dc)

                    if validCheat:
                        sub_time = BFS((nr, nc), cheats - 1)
                        print(f"Cheated on {(r + dr, c + dc)} to {(nr, nc)}, subpath was {sub_time}")
                        if cheats - 1 == 0 and sub_time >= 0:
                           times.append(sub_time + time + 20)

                elif grid[r + dr][c + dc] != "#":
                    queue.append((r + dr, c + dc, time + 1))

    cache[(start, cheats)] = -1
    return -1

base_time = BFS(start, cheats=0)
print("finished with base run")
BFS(start)
print(len([base_time - t for t in times if base_time - t >= 100]))

#
# # For part 1 testing
# print(times)
# times = [base_time - t for t in times if base_time - t > 0]
# print(Counter(times))

