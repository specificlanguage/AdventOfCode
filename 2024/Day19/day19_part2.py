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

# the question is now how many ways can you make it? we could just do the simple splice and dice.
def can_make(design):
    if design == "":
        return 1
    if design in can_make_cache:
        return can_make_cache[design]

    total_ways = 0
    for pattern in patterns:
        l = len(pattern)
        if design[:l] == pattern:
            subways = can_make(design[l:])
            total_ways += subways

    can_make_cache[design] = total_ways
    return total_ways

ans = 0

for design in designs:
    num_ways = can_make(design)
    print(num_ways, design)
    ans += num_ways

print(ans)


