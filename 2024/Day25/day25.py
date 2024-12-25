import heapq
import queue
from collections import defaultdict, deque, Counter
from functools import cache
import itertools
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day25input'

locks = []
keys = []

with open(FILEPATH) as f:
    grids = f.read().split("\n\n")


def lockHeight(grid):
    heights = []
    for c in range(len(grid[0])):
        for r in range(len(grid)):
            if grid[r][c] == '.':
                heights.append(r - 1)
                break
    return heights


def keyHeight(grid):
    heights = []
    for c in range(len(grid[0])):
        for r in range(len(grid)-1, -1, -1):
            if grid[r][c] == '.':
                heights.append(len(grid) - r - 2)
                break
    return heights

def validCombo(lock, key):
    for col in range(len(lock)):
        if key[col] + lock[col] > 5:
            return False
    return True

for grid in grids:
    ig = grid.split("\n")
    if ig[0] == "#" * 5:
        locks.append(lockHeight(ig))
    else:
        keys.append(keyHeight(ig))

valid = 0
for l in locks:
    for k in keys:
        valid += 1 if validCombo(l, k) else 0

print(valid)
