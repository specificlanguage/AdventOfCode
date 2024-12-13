from collections import defaultdict
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day13input'
PART = 2
NUM = 10000000000000
lines = []
ans = 0

def calcMoves(buttonA, buttonB, prize):

    # I have to remember from algebra 2:
    # a1x + b1x = px
    # a2y + b2y = p2y
    a1, a2 = buttonA
    b1, b2 = buttonB
    p1, p2 = (x if PART == 1 else x + NUM for x in prize)

    y = (p1 * a2 - p2 * a1) / (a2 * b1 - a1 * b2)
    x = (p1 * b2 - p2 * b1) / (a1 * b2 - a2 * b1)
    return x, y

with open(FILEPATH) as f:
    for line in f:
        lines.append(line)
    buttonA = (-1, -1)
    buttonB = (-1, -1)
    target = (-1, -1)
    # print(lines)

    for i in range(len(lines)):
        if i % 4 == 0:  # Button A
            m = re.match(r'Button A: X\+(\d+), Y\+(\d+)', lines[i])
            buttonA = tuple(int(x) for x in m.group(1, 2))
        elif i % 4 == 1:
            m = re.match(r'Button B: X\+(\d+), Y\+(\d+)', lines[i])
            buttonB = tuple(int(x) for x in m.group(1, 2))
        elif i % 4 == 2:
            m = re.match(r'Prize: X=(\d+), Y=(\d+)', lines[i])
            target = tuple(int(x) for x in m.group(1, 2))
        elif i % 4 == 3: # Calculate

            A, B = calcMoves(buttonA, buttonB, target)

            # Dumb checks
            if A % 1 == 0 and B % 1 == 0:
                # print(i // 4, A, B)
                ans += round(A)*3 + round(B)

    print(ans)



