# Part 1 code (and, really part 2 since not much of it was changed
# has been pretty much lifted from https://github.com/xHyroM/aoc/blob/main/2023/12/first.py

from functools import cache

FILENAME = "d12input"

records = []
for line in open(FILENAME).readlines():
    line = line.strip()
    pattern, counts = line.split()
    counts = tuple(int(x) for x in counts.split(",")) * 5
    pattern = "?".join([pattern] * 5)
    records.append((pattern, counts))

# Cache is required in part 2 for a lot of dynamic programming-like aspects
@cache
def calc_arrangements(pattern: str, counts: tuple[int]) -> int:
    if not pattern:
        return len(counts) == 0
    if not counts:
        return "#" not in pattern
    result = 0

    if pattern[0] in ".?":  # In unknown spot, keep recursing
        result += calc_arrangements(pattern[1:], counts)

    # In known spot, check to see if we're in a pattern
    if pattern[0] in "#?" and \
            counts[0] <= len(pattern) and \
            "." not in pattern[:counts[0]] and \
            (counts[0] == len(pattern) or pattern[counts[0]] != "#"):
        result += calc_arrangements(pattern[counts[0] + 1 :], counts[1:])

    return result

total = 0
for i, (pattern, count) in enumerate(records):
    print("Parsing pattern", i, " (length", len(count), ")")
    total += calc_arrangements(pattern, count)
print(total)
