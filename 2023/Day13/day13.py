# Heavily inspired from https://github.com/TimFanelle/AdventOfCode/blob/main/2023/13-partOne.py

FILENAME = "d13input"

puzzles = []
with open(FILENAME) as textIn:
    puzz = []
    for line in textIn:
        if line != '\n':
            puzz.append(line.strip())
        else:
            puzzles.append(puzz)
            puzz = []
    puzzles.append(puzz)


def isSmudgy(rowA, rowB):
    smudgeCount = 0
    for i in range(len(rowA)):
        if rowA[i] != rowB[i]:
            smudgeCount += 1
    return smudgeCount

def isSymmetrical(puzzle):
    smudges = 0
    if len(puzzle) <= 1:
        return False
    for i in range(len(puzzle) // 2):
        smudges += isSmudgy(puzzle[i], puzzle[-i-1])
    return smudges == 1


def determineMirror(puzzle):
    for rowNum in range(len(puzzle)):
        if (rowNum + 1) * 2 < len(puzzle):
            temp = isSymmetrical(puzzle[:(rowNum + 1) * 2])
        else:
            temp = isSymmetrical(puzzle[-((len(puzzle) - 1) - rowNum) * 2:])
        if temp:
            return rowNum + 1
    return None

total = 0
for i in range(len(puzzles)):
    print("Puzzle", i, "has", len(puzzles[i]), "rows,", len(puzzles[i][0]), "columns.")
    rowReflect = determineMirror(puzzles[i])
    print(rowReflect * 100 if rowReflect else 0)
    if rowReflect:
        total += rowReflect * 100
    else:
        total += determineMirror(list(zip(*(puzzles[i]))))
print(total)
