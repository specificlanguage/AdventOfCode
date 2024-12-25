import heapq
import queue
from collections import defaultdict, deque, Counter
from functools import cache
import itertools
from keyword import kwlist
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day24input'
init_bools, equations, lineage = {}, {}, {}

with open(FILEPATH) as f:
    vals, eqs = f.read().split("\n\n")
    for line in vals.split("\n"):
        key, val = re.match(r"(.{3}): ([01])", line).groups()
        init_bools[key] = int(val)
    for equation in eqs.split("\n"):
        k1, op, k2, output = re.match(r"(.{3}) (XOR|OR|AND) (.{3}) -> (.{3})", equation).groups()
        equations[(k1, op, k2)] = output
        lineage[output] = [k1, k2, op]

# Convert to binary number
def toBinary(letter, bools):
    return "".join(reversed([str(k[1]) for k in sorted([(k,v) for k,v in bools.items() if k[0] == letter])]))

# Try to answer as you can. O(n^2) iteration here, but whatever.
def calculate(equations):
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
    return toBinary("z", bools)

x = toBinary("x", init_bools)
y = toBinary("y", init_bools)
z = calculate(equations)
print(x, y, z)

faulty_ops = []
and_gates = set(output for output in lineage if lineage[output][2] == "AND" and lineage[output][1][0] in ["x", "y"] and lineage[output][0][0] in ["x", "y"])
xor_gates = set(output for output in lineage if lineage[output][2] == "XOR" and lineage[output][1][0] in ["x", "y"] and lineage[output][0][0] in ["x", "y"])
for output in lineage:
    k1, k2, op = lineage[output]
    if output[0] == "z":
        if op != "XOR":
            faulty_ops.append(output)
    if output[0] != "z" and k1[0] not in ["x", "y"] and k2[0] not in ["x", "y"]:
        if op == "XOR":
            faulty_ops.append(output)
    if op == "OR":
        and_gates.discard(k1)
        and_gates.discard(k2)
    if op == "XOR":
        xor_gates.discard(k1)
        xor_gates.discard(k2)

print(faulty_ops)
print(and_gates)
print(xor_gates)
print(",".join(sorted(['frt', 'z11', 'z23', 'z05', 'sps', 'tst', 'cgh', 'pmd'])))

# def diagnoseLineage(bit, level=0):
#     if bit[0] == "y" or bit[0] == "x":
#         print("  " * level + f"{bit} : {bools[bit]}")
#         return
#     k1, k2, op = lineage[bit]
#     v1, v2, vb = bools[k1], bools[k2], bools[bit]
#     print("  " * level + f"{k1} {op} {k2} = {bit} : ({v1} {op} {v2} = {vb})")
#     diagnoseLineage(k1, level + 1)
#     diagnoseLineage(k2, level + 1)
#
# def verify(x, y, z):
#     x = x[::-1]
#     y = y[::-1]
#     z = z[::-1]
#     carry = 0
#     for i in range(len(x)):
#         add = int(x[i]) + int(y[i]) + carry
#         res, next_carry = add % 2, add // 2
#         if res != int(z[i]):
#             print("incorrect bit", i, f"z{i:02}: {x[i]}, y{i:02}: {y[i]}, z{i:02}: {z[i]}, carry: {carry}")
#             diagnoseLineage(bit=f"z{i:02}")
#             print("----------------------")
#         carry = next_carry

# verify(x, y, z)
# for i in range(6):
#     diagnoseLineage(bit=f"z{i:02}")

# z05,