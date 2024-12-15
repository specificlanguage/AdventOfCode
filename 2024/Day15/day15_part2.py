from collections import defaultdict, deque
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

def display_grid(grid):
    print("\n".join("".join(col for col in row) for row in grid))

num_boxes = 0

new_grid = [[] for r in grid]

# Find starting point, oops.
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "#":
            new_grid[r].extend(["#", "#"])
        elif grid[r][c] == "O":
            new_grid[r].extend(["[", "]"])
        elif grid[r][c] == ".":
            new_grid[r].extend([".", "."])
        elif grid[r][c] == "@":
            startr, startc = r, c * 2
            new_grid[r].extend(["@", "."])

grid = new_grid
display_grid(grid)
ROWS, COLS = len(grid), len(grid[0])

def moveDir(orig_r, orig_c, dr, dc):
    # This will be a stack tracking the last position that we checked
    toMove = set()
    toVerify = deque([(orig_r, orig_c)])

    while toVerify:
        r, c = toVerify.pop()
        if (r, c) in toMove:       # Already verified, no need to change.
            continue
        if grid[r][c] == "#":
            return orig_r, orig_c  # No change, run into wall

        # Extra dependencies to check:
        if grid[r][c] == "[":    # Need to depend on its right cousin.
            toVerify.append((r, c+1))
        elif grid[r][c] == "]":
            toVerify.append((r, c-1))
        if grid[r][c] != ".":
            toMove.add((r, c))
            toVerify.append((r + dr, c + dc))

    toPlace = set()
    while toMove:
        r, c = toMove.pop()
        item = grid[r][c]
        grid[r][c] = '.'
        r += dr; c += dc
        toPlace.add((r, c, item))
    while toPlace:
        r, c, item = toPlace.pop()
        grid[r][c] = item

    return orig_r + dr, orig_c + dc

row, col = startr, startc
print(row, col)

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
        if grid[i][j] == "[":
            # num_boxes += 1
            print(f"Box {num_boxes}, {i}, {j}: {100 * i + j}")
            ans += 100 * i + j

print(ans)




