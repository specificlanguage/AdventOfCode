import heapq
from collections import defaultdict, deque
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day18input'
lines = []
LENGTH = 71
LIMIT = 1024

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def generate_grid():
    return [["." for _ in range(LENGTH)] for _ in range(LENGTH)]

def display_grid(grid):
    print("\n".join("".join(col for col in row) for row in grid))

with open(FILEPATH) as f:
    for line in f:
        if line != "":
            c, r = (int(x) for x in line.strip().split(","))
            lines.append((r, c))

grid = generate_grid()

for x in range(LIMIT):
    r, c = lines[x]
    print(r, c)
    grid[r][c] = "#"

display_grid(grid)

def findExit():
    queue = deque([(0, 0, 0)]) # r, c, score
    visited = set()
    while queue:
        r, c, length = queue.popleft()
        if (r, c) == (LENGTH - 1, LENGTH - 1): # The goal!
            return length
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in dirs:
            if 0 <= r + dr < LENGTH and 0 <= c + dc < LENGTH \
                    and grid[r + dr][c + dc] != "#" and (r + dr, c + dc) not in visited:
                queue.append((r + dr, c + dc, length + 1))
    return -1

print(findExit())