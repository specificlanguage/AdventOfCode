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

def findContiguousSides(segments):
    sides = 0
    for set in segments:
        for i in segments[set]:
            if i - 1 not in segments[set]: # Checks for a contiguous side.
                sides += 1
    return sides


def findRegionStats(start):
    queue = [start]
    startr, startc = start
    region_letter = lines[startr][startc]
    area, perimeter = 0, 0
    visited = set()

    up_segments = defaultdict(set)
    down_segments = defaultdict(set)
    right_segments = defaultdict(set)
    left_segments = defaultdict(set)


    while queue:
        r, c = queue.pop()
        if (r, c) not in visited:
            visited.add((r, c))
            regions[(r, c)] = startr, startc
            area += 1
            for dr, dc, dir in directions:
                nr, nc = r + dr, c + dc # New coordinates
                if -1 <= nr <= m and -1 <= nc <= n:
                    if nr in (-1, m) or nc in (-1, n) or lines[nr][nc] != region_letter:
                        perimeter += 1  # Next edge is not the same, counts as perimeter.

                        # We are going to store the 'row' of the edge here,
                        # attached to the left 'index' of the edge it's associated to.
                        # print(nr, nc, dir)

                        if dir == 'u':
                            # print("row edge", r, c)
                            up_segments[r].add(c)
                        elif dir == 'd':
                            # print("row edge", r+1, c)
                            down_segments[r+1].add(c)
                        # Similarly, we will store the edge 'column' it's located
                        # Then the top-most row it's allocated to.
                        elif dir == 'l':
                            # print("col edge", r, c)
                            left_segments[c].add(r)
                        else:
                            # print("col edge", r, c+1)
                            right_segments[c+1].add(r)
                    else:
                        queue.append((nr, nc))

    segments = [up_segments, down_segments, right_segments, left_segments]

    sides = sum(
        [findContiguousSides(s) for s in segments]
    )

    return area, perimeter, sides

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if (i, j) not in regions: # Start of new region
            area, perim, sides = findRegionStats((i, j))
            ans += area * sides

print(ans)