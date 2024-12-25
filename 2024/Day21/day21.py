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

    possible_paths = []

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
            possible_paths.append("".join(perm))

    return possible_paths


def calcNumpadRoute(numpad):
    paths = {''}
    curr_r, curr_c = numpad_layout["A"]

    for key in numpad:
        next_paths = set()
        next_r, next_c = numpad_layout[key]
        poss_paths = findValidSeq(curr_r, curr_c, next_r, next_c, numpad=True)

        for key_path in poss_paths:
            for base_path in paths:
                next_paths.add(base_path + key_path + "A")
        paths = next_paths
        curr_r, curr_c = next_r, next_c

    return paths

def calcKeypadRoute(numpad, level=1):
    if level == 1:
        paths_to_calc = calcNumpadRoute(numpad)
    else:
        paths_to_calc = calcKeypadRoute(numpad, level - 1)

    curr_r, curr_c = keypad_layout["A"]
    final_paths = set()
    min_path_length = float("inf")

    for path in paths_to_calc:
        paths = {''}
        for key in path:
            next_paths = set()
            next_r, next_c = keypad_layout[key]
            poss_paths = findValidSeq(curr_r, curr_c, next_r, next_c)

            for key_path in poss_paths:
                for base_path in paths:
                    next_paths.add(base_path + key_path + "A")
            paths = next_paths
            curr_r, curr_c = next_r, next_c

        final_paths = final_paths.union(paths)

    return final_paths

ans = 0
for line in lines:
    routes = calcKeypadRoute(line, 2)
    num = int(line[:-1])
    min_route_length = min(len(x) for x in routes)
    min_route = min([(len(x), x) for x in routes])
    print(num, min_route_length)
    ans += num * min_route_length

print(ans)