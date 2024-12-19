import heapq
from collections import defaultdict, deque
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day19input'
lines = []

with open(FILEPATH) as f:
    patterns, designs = f.read().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.split("\n")

# patterns.sort(key=lambda x: len(x), reverse=True) # Sort in reverse order to limit calls
can_make_cache = {}

def can_make(design):
    if design == "":
        return True
    if design in can_make_cache:
        return can_make_cache[design]
    for pattern in patterns:
        l = len(pattern)
        if design[:l] == pattern:
            ans = can_make(design[l:])
            if ans:
                can_make_cache[design] = ans
                return True
    can_make_cache[design] = False
    return False

ans = 0

for design in designs:
    if can_make(design):
        print("can make", design)
        ans += 1
    else:
        print("cannot make", design)

print(ans)


