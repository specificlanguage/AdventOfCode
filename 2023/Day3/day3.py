# Well, I thought I might have had the answer before, but who knows man.
# I thought I could do it without looking at Regex, but it looks like I might have to now.

import re
from math import prod
from collections import defaultdict

with open("d3input.txt") as f:
    lines = f.read().split("\n")

symbols = dict()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c not in "1234567890.":
            symbols[(x, y)] = c

parts = defaultdict(list)
total = 0

for x, y in symbols:
    for line in (lines[y-1:y+2]):
        for num in re.finditer(r"\d+", line):
            start, end = num.start(), num.end()
            if start - 1 <= x <= end:
                part = int(num.group())
                parts[(x, y)].append(part)
                total += part

# PART ONE
print(total)

# PART TWO
gearRatios = 0
for x, y in symbols:
    if symbols[(x, y)] == "*" and len(parts[(x, y)]) > 1:
        gearRatios += prod(parts[(x, y)])
print(gearRatios)