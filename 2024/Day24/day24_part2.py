import heapq
import queue
from collections import defaultdict, deque, Counter
from functools import cache
import itertools
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day24input'
init_bools = {}
equations = {}
lineage = {}

with open(FILEPATH) as f:
    vals, eqs = f.read().split("\n\n")
    for line in vals.split("\n"):
        key, val = re.match(r"(.{3}): ([01])", line).groups()
        init_bools[key] = int(val)
    for equation in eqs.split("\n"):
        k1, op, k2, output = re.match(r"(.{3}) (XOR|OR|AND) (.{3}) -> (.{3})", equation).groups()
        equations[(k1, op, k2)] = output
        lineage[output] = [k1, k2]

# Try to answer as you can. O(n^2) iteration here, but whatever.
def calculate():
    to_eval = deque(equations.items())
    bools = init_bools.copy()

    while to_eval:
        key, output = to_eval.popleft()
        k1, op, k2 = key
        if k1 in bools and k2 in bools:
            if op == "AND":
                bools[output] = bools[k1] and bools[k2]
            elif op == "OR":
                bools[output] = bools[k1] or bools[k2]
            elif op == "XOR":
                bools[output] = bools[k1] ^ bools[k2]
        else:
            to_eval.append((key, output))
    return retrieveBinaryNumber("z", bools)

def retrieveBinaryNumber(letter, bools):
    return int("".join(reversed([str(k[1]) for k in sorted([(k,v) for k,v in bools.items() if k[0] == letter])])), 2)

def findIncorrectBits(a, b):
    bits = []
    a, b = f'{a:b}', f'{b:b}'
    for i in range(len(a)): # Assuming it is the same length as b
        if a[i] != b[i]:
            bits.append(len(a) - i - 1)
    return bits

def findLineage(bit_number):
    ret = set()
    queue = deque([f"z{bit_number:02}"])
    while queue:
        key = queue.popleft()
        ret.add(key)
        if key in lineage:
            for desc in lineage[key]:
                queue.append(desc)
    return ret

def genCandidatesToSwap(z):

    def uniqueItems(x): # Need to check if all items within the combo list are unique.
        seen = set()
        for t in x:
            for n in t:
                if n in seen: return False
                seen.add(n)
        return True

    # Convert to binary number
    x = retrieveBinaryNumber("x", init_bools)
    y = retrieveBinaryNumber("y", init_bools)
    ibs = findIncorrectBits(x + y, z)
    candidates = []
    for bs in ibs:
        suspects = findLineage(bs)
        for sus in suspects:
            if not re.match(r"[x|y]\d{2}", sus):
                candidates.append(sus)

    # Generate all pairwise swaps
    swaps = itertools.combinations(candidates, 2)

    # Generate all possible four-sets
    four_sets = itertools.combinations(swaps, 4)
    return filter(uniqueItems, four_sets)

z = calculate()
swap_possibilities = genCandidatesToSwap(z)
for x in swap_possibilities:
    print(x)




