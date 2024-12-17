import heapq
from collections import defaultdict, deque
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day17test'
lines = []

with open(FILEPATH) as f:
    lines = f.readlines()

A = int(re.match(r"Register A: (\d+)", lines[0]).group(1))
B = int(re.match(r"Register B: (\d+)", lines[1]).group(1))
C = int(re.match(r"Register C: (\d+)", lines[2]).group(1))
program = re.match(r"Program: ((\d,?)+)", lines[4])
program = [int(p) for p in program.groups()[0].split(",")]
# print(program)

def convertToCombo(code):
    if code < 4:
        return code
    elif code == 4:
        return A
    elif code == 5:
        return B
    elif code == 6:
        return C
    raise ValueError("Invalid code")

output = []

def run_program(codes):
    global A, B, C
    tape_location = 0

    print(f"A: {A}, B: {B}, C: {C}")

    while tape_location < len(codes):
        instr, operand = codes[tape_location], codes[tape_location + 1]
        print(f"Executing {instr} | {operand} (tape location {tape_location})")

        if instr == 0:  # adv, division
            A =  A // (2**(convertToCombo(operand)))
        elif instr == 1:
            B ^= operand
        elif instr == 2:
            B = convertToCombo(operand) % 8
        elif instr == 3: # skipper -- it just so happens the only time this is used is to go to start.
            if A == 0: pass
            else: tape_location = operand
        elif instr == 4: # Bxc
            B = C ^ B
        elif instr == 5: # out
            output.append(convertToCombo(operand) % 8)
            print(output)
        elif instr == 6:
            B = A // (2 ** convertToCombo(operand))
        elif instr == 7:
            C = A // (2 ** convertToCombo(operand))

        if (instr == 3 and A != 0) or instr != 3:
            tape_location += 2

        # print(f"A: {A}, B: {B}, C: {C}")
        # print("------------")

# Tester code, ignore
run_program(program)
print(",".join(str(o) for o in output))



