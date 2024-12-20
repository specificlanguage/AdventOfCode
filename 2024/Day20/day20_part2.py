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

def retrieveCheats(source_r, source_c): # Cheats originating from wall node (r, c). Find cells within 20 manhattan.
    locations = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            manhattan = abs(r - source_r) + abs(c - source_c)
            if manhattan <= 20 and grid[r][c] != "#":
                locations.append((r, c, manhattan))
    return locations

times = []
dist_from_start = {}

def BFS_Base(start):
    start_r, start_c = start
    queue = deque([(start_r, start_c, 0)])

    while queue:
        r, c, time = queue.popleft()
        if (r, c) in dist_from_start:
            continue
        dist_from_start[(r, c)] = time
        if grid[r][c] == 'E':
            return time
        for dr, dc in dirs:
            if 0 <= r + dr < M and 0 <= c + dc < N and grid[r + dr][c + dc] != '#':
                queue.append((r + dr, c + dc, time + 1)) # Cheating!


def BFS_Cheat(start, base_time):
    start_r, start_c = start
    queue = deque([(start_r, start_c)])
    already_seen = set()
    calculated = set()

    while queue:
        r, c = queue.popleft()
        if (r, c) in already_seen:
            continue
        already_seen.add((r, c))

        exits = retrieveCheats(r, c)
        for nr, nc, cheat_time in exits:
            find_time = cheat_time + dist_from_start[(r, c)] + base_time - dist_from_start[(nr, nc)]
            times.append(find_time)

        for dr, dc in dirs:
            if 0 <= r + dr < M and 0 <= c + dc < N and grid[r + dr][c + dc] != '#':
                queue.append((r + dr, c + dc))

base_time = BFS_Base(start)
BFS_Cheat(start, base_time)
print(len([base_time - t for t in times if base_time - t >= 100]))

#
# # For testing
# print(times)
# times = [base_time - t for t in times if base_time - t >= 50]
# print(sorted(dict(Counter(times)).items()))

