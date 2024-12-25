import heapq
import queue
from collections import defaultdict, deque, Counter
from functools import cache
import itertools
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day24input'
bools = {}
equations = deque()

with open(FILEPATH) as f:
    vals, eqs = f.read().split("\n\n")
    for line in vals.split("\n"):
        key, val = re.match(r"(.{3}): ([01])", line).groups()
        bools[key] = int(val)
    for equation in eqs.split("\n"):
        k1, op, k2, output = re.match(r"(.{3}) (XOR|OR|AND) (.{3}) -> (.{3})", equation).groups()
        equations.append((k1, k2, op, output))

# Try to answer as you can. O(n^2) iteration here, but whatever.
while equations:
    k1, k2, op, output = equations.popleft()
    if k1 in bools and k2 in bools:
        if op == "AND":
            bools[output] = bools[k1] and bools[k2]
        elif op == "OR":
            bools[output] = bools[k1] or bools[k2]
        elif op == "XOR":
            bools[output] = bools[k1] ^ bools[k2]
    else:
        equations.append((k1, k2, op, output))

# Convert to binary number
z = "".join(reversed([str(k[1]) for k in sorted([(k,v) for k,v in bools.items() if k[0] == 'z'])]))
print(int(z, 2))







