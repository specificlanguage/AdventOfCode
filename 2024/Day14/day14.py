from collections import defaultdict
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day14input'
PART = 2
lines = []
ans = 0
ROWS, COLS = 103, 101

def simulate(pr, pc, vr, vc, n = 5):
    for i in range(n):
        pr += vr
        pc += vc
        pr %= ROWS
        pc %= COLS
    return pr, pc

q1 = q2 = q3 = q4 = 0


with open(FILEPATH) as f:
    for line in f:
        matches = re.match(r'^p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
        pc, pr, vc, vr = [int(i) for i in matches.groups()]

        er, ec = simulate(pr, pc, vr, vc, 100)

        if ec > COLS // 2:
            if er > ROWS // 2:
                q1 += 1
            elif er < ROWS // 2:
                q2 += 1
        elif ec < COLS // 2:
            if er > ROWS // 2:
                q3 += 1
            elif er < ROWS // 2:
                q4 += 1

print(q1, q2, q3, q4)

ans = q1 * q2 * q3 * q4
print(ans)