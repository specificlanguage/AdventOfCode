from collections import defaultdict
from math import log10, floor

FILEPATH = 'day12input'

lines = []
ans = 0

with open(FILEPATH) as f:
    for line in f:
        lines.append([n for n in line.strip()])

m, n = len(lines), len(lines[0])
regions = {}
directions = [(0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u')]

visited = set()

def findRegionStats(start):
    queue = [start]
    startr, startc = start
    region_letter = lines[startr][startc]
    area, perimeter = 0, 0

    while queue:
        r, c = queue.pop()
        if (r, c) not in visited:
            visited.add((r, c))
            area += 1
            for dr, dc, dir in directions:
                nr, nc = r + dr, c + dc # New coordinates
                if -1 <= nr <= m and -1 <= nc <= n:
                    if nr in (-1, m) or nc in (-1, n) or lines[nr][nc] != region_letter:
                        perimeter += 1  # Next edge is not the same, counts as perimeter.
                    else:
                        queue.append((nr, nc))

    return area, perimeter

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if (i, j) not in regions: # Start of new region
            area, perim = findRegionStats((i, j))
            ans += area * perim

print(ans)