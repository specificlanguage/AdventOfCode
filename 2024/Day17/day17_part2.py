import heapq
from collections import defaultdict, deque
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day17input'
lines = []

with open(FILEPATH) as f:
    lines = f.readlines()

A = int(re.match(r"Register A: (\d+)", lines[0]).group(1))
B = int(re.match(r"Register B: (\d+)", lines[1]).group(1))
C = int(re.match(r"Register C: (\d+)", lines[2]).group(1))
program = re.match(r"Program: ((\d,?)+)", lines[4])
program = [int(p) for p in program.groups()[0].split(",")]

output = []

def run_program(codes, A):

    B, C = 0, 0
    tape_location = 0


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

    # print(f"A: {A}, B: {B}, C: {C}")

    while tape_location < len(codes):
        instr, operand = codes[tape_location], codes[tape_location + 1]

        if instr == 0:  # adv, division
            A =  A // (2**(convertToCombo(operand)))
        elif instr == 1:
            B ^= operand
        elif instr == 2:
            B = convertToCombo(operand) % 8
        elif instr == 3: # skipper -- it just so happens the only time this is used is to go to start.
            break
        elif instr == 4: # Bxc
            B = C ^ B
        elif instr == 5: # out
            return convertToCombo(operand) % 8
        elif instr == 6:
            B = A // (2 ** convertToCombo(operand))
        elif instr == 7:
            C = A // (2 ** convertToCombo(operand))

        tape_location += 2

# Use this code to calculate your next move
while A != 0:
    print(A)
    x = run_program(program, A)
    print(A, x)
    A //= 8 # This happens to be the code that always happens for me, so like, whatever.
    # Bad practice, but kill me.

# print("229:", run_program(program, 28))

outputs = list(reversed(program))
queue = deque([(0, 0)]) # Base number, 0

while queue:
    base, index = queue.popleft()
    # print(queue)
    if index == len(outputs): # you have the result for the next one, but need to check
        print(base // 8)
        break
    else:
        for i in range(8): # Reverse engineer the way up
            result = run_program(program, base + i)
            if result == outputs[index]:
                queue.append(((base + i) * 8, index + 1))