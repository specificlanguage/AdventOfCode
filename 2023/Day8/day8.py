import math
from functools import reduce

FILENAME = "d8input"

conns = {}
starts = []

with open(FILENAME) as file:
    SEQUENCE = file.readline().strip()
    lines = []
    file.readline()  # Skip empty line
    for line in file:
        node, leftConn, rightConn = line[:3], line[7:10], line[12:15]
        conns[node] = (leftConn, rightConn)
        if node[-1] == "A":
            starts.append(node)

nextZ = []

def findNextZ(node):
    total = 0
    curr = node
    while True:

        for direct in SEQUENCE:
            total += 1
            if direct == "L":
                curr = conns[curr][0]
            if direct == "R":
                curr = conns[curr][1]
            if curr[-1] == "Z":
                return total

for node in starts:
    nextZ.append(findNextZ(node))

print(reduce(lambda x, y: math.lcm(x, y), nextZ))
