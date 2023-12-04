import math

FNAME = "d3input.txt"


with open(FNAME) as f: # Get number of lines in file
    rowcount = sum(1 for _ in f)

numbers = [[] for _ in range(rowcount)]
visited = {}
answer = 0

# Load numbers into the respective rows as a lookup table
def registerNums(row: int, s: str):
    currentNumber = ""
    for i in range(len(s)):
        if s[i].isnumeric():
            currentNumber += s[i]
        elif currentNumber != "":
            # Insert into table where the
            part = int(currentNumber)
            numbers[row].append((part, row, int(i-math.log10(part)), i-1))
            currentNumber = ""

def getPartsNumber(row: int, col: int):
    lookups = []
    if row > 0:
        lookups += numbers[row-1]
    if row < rowcount:
        lookups += numbers[row+1]
    lookups += numbers[row]
    # print(lookups, row, col)
    for number, numRow, start, end in lookups:
        if number not in visited and (start - 1 <= col <= end + 1):
            # print(number, numbers[numRow])
            global answer
            answer += number
            numbers[numRow].remove((number, numRow, start, end))

with open(FNAME) as f: # Insert numbers into lookup table
    for i in range(rowcount):
        registerNums(i, f.readline())

with open(FNAME) as f:
    for i in range(rowcount):
        for j, ch in enumerate(f.readline()):
            if not ch.isnumeric() and ch not in ".\n":
                getPartsNumber(i, j)

print(answer)

