import heapq
from collections import defaultdict, deque, Counter
from functools import cache
from itertools import permutations
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day21input'
lines = []

with open(FILEPATH) as f:
    for line in f:
        lines.append(line.strip())

numpad_layout = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
                 "0": (3, 1), "A": (3, 2)
}

keypad_layout = {
                 "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2)
}

@cache
def findValidSeq(start_r, start_c, dest_r, dest_c, numpad=False):
    if numpad:
        excluded = {(3, 0)}
    else:
        excluded = {(0, 0)}
    path = []
    diff_r = dest_r - start_r
    diff_c = dest_c - start_c
    if diff_r > 0: path.extend(["v"] * abs(diff_r))  # next_r is right of curr_r, so >
    elif diff_r < 0: path.extend(["^"] * abs(diff_r))  # next_r is left of curr_r
    if diff_c > 0: path.extend([">"] * abs(diff_c))
    elif diff_c < 0: path.extend(["<"] * abs(diff_c))

    possible_paths = set()

    for perm in permutations(path):
        r, c = start_r, start_c
        valid = True
        for direc in perm:
            if direc == ">": c += 1
            elif direc == "<": c -= 1
            elif direc == "^": r -= 1
            elif direc == "v": r += 1
            if (r, c) in excluded: # Invalid path, explosion!
                valid = False
                break
        if valid:
            possible_paths.add("".join(perm))

    return list(possible_paths)

def findPath(keys, index, prevKey, currPath, result, numpad=False):
    if index == len(keys):
        result.append("".join(currPath))
        return
    sr, sc = keypad_layout[prevKey] if not numpad else numpad_layout[prevKey]
    er, ec = keypad_layout[keys[index]] if not numpad else numpad_layout[keys[index]]
    for possPath in findValidSeq(sr, sc, er, ec, numpad):
        findPath(keys, index+1, keys[index], currPath + possPath + "A", result, numpad)

@cache
def shortestSeq(keys, depth):
    if depth == 0:
        return len(keys)

    subkeys = re.split("([\^v<>]*A)", keys) # remove the final character since it's useless
    subkeys = [s for s in subkeys if s != ""]
    total = 0
    for subkey in subkeys:
        result = []
        findPath(subkey, 0, "A", "", result)
        total += min(shortestSeq(seq, depth - 1) for seq in result)
    return total

def solve(numpad, depth):
    total = 0
    numpadPaths = []
    findPath(numpad, 0, "A", "", numpadPaths, numpad=True)
    total += min(shortestSeq(seq, depth) for seq in numpadPaths)
    return total

ans = 0
for line in lines:
    x = solve(line, 25)
    ans += x * int(line[:-1])
print(ans)

