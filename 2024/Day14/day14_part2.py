from collections import defaultdict, deque
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day14input'
PART = 2
lines = []
ans = 0
ROWS, COLS = 103, 101

def display_grid(points):
    grid = [[" " for i in range(COLS)] for i in range(ROWS)]
    for pr, pc in points:
        grid[pr][pc] = "#"
    return "\n".join(["".join(row) for row in grid])

def simulate(pr, pc, vr, vc):
    pr += vr
    pc += vc
    pr %= ROWS
    pc %= COLS
    return pr, pc

def search(points: set[tuple[int, int]]):

    found = 0
    pr, pc = points.pop()
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)]
    queue = deque([(pr, pc)])
    # Keep searching until you've found everything in the set.
    while queue:
        pr, pc = queue.pop()
        for dr, dc in dirs:
            if 0 <= pr + dr < ROWS and 0 <= pc + dc < COLS \
                    and (pr + dr, pc + dc) in points:
                found += 1
                points.remove((pr + dr, pc + dc))
                queue.append((pr + dr, pc + dc))
    return found

points = set()

with open(FILEPATH) as f:
    for line in f:
        matches = re.match(r'^p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
        pc, pr, vc, vr = [int(i) for i in matches.groups()]
        points.add((pr, pc, vr, vc))

print(49761 - 39358) # This was my cycle number, sorry!

for i in range(10403):
    ans += 1
    # if ans % 100 == 0:
    #     print("iteration", ans)
    new_points = set()
    for pr, pc, vr, vc in points:
        er, ec = simulate(pr, pc, vr, vc)
        new_points.add((er, ec, vr, vc))
    coords = set((x, y) for x, y, _, _ in new_points)
    search_score = search(coords)
    if search_score == len(coords):
        print(ans)
        break

    # Simply the strategy is not to find a Christmas tree,
    # but a significant amount of contiguous robots that constitute a "shape".
    if search_score > 50:
        with open(f"output_{ans}", "w") as f:
            f.write(display_grid(set((x, y) for x, y, _, _ in new_points)))
        print(f"found something close! {search_score} at iteration {ans}",)
    points = new_points


