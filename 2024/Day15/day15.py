from collections import defaultdict
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day15input'
lines = []
startr, startc = 0, 0
boxes = set()

with open(FILEPATH) as f:
    str = f.read()
    grid, directions = str.split("\n\n")

grid = [[e for e in r] for r in grid.split("\n")]
ROWS, COLS = len(grid), len(grid[0])

def display_grid(grid):
    print("\n".join("".join(col for col in row) for row in grid))

num_boxes = 0

# Find starting point, oops.
for r in range(len(grid)):
    for c in range(len(grid[0])):
        # if grid[r][c] == "O":
        #     num_boxes += 1
        #     print(f"Box {num_boxes}, {r}, {c}")

        if grid[r][c] == "@":
            startr, startc = r, c


def moveDir(r, c, dr, dc):
    # This will be a stack tracking the last position that we checked
    toMoveUp = [(r, c)]

    while True:
        lastr, lastc = toMoveUp[-1]
        if grid[lastr + dr][lastc + dc] == "#":  # Next position is a wall
            # print("wall in way", lastr + dr, lastc + dc)
            return r, c
        elif grid[lastr + dr][lastc + dc] == "O":  # Next position is a box, we keep going
            # print("adding box")
            toMoveUp.append((lastr + dr, lastc + dc))
            continue
        else:   # We are not pushing a wall nor a box, we can move now.
            # print("we're finally moving!")
            break

    while toMoveUp:
        r, c = toMoveUp.pop()
        grid[r][c] = '.'
        r += dr; c += dc
        if len(toMoveUp) == 0:
            grid[r][c] = "@"
        else:  # Remove the box!
            grid[r][c] = "O"

    return r, c

row, col = startr, startc

for dir_chr in directions:
    if dir_chr == "^":
        row, col = moveDir(row, col, -1, 0)
    elif dir_chr == "v":
        row, col = moveDir(row, col, 1, 0)
    elif dir_chr == "<":
        row, col = moveDir(row, col, 0, -1)
    elif dir_chr == ">":
        row, col = moveDir(row, col, 0, 1)

    # display_grid(grid)

# Find boxes

ans = 0
num_boxes = 0
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == "O":
            # num_boxes += 1
            # print(f"Box {num_boxes}, {i}, {j}")
            ans += 100 * i + j

print(ans)




