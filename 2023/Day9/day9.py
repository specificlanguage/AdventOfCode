FILENAME = "d9input"

numbers = []

with open(FILENAME) as file:
    for line in file:
        numbers.append([int(x) for x in line.strip().split(" ")])

def findDiffs(arr):
    return[arr[i] - arr[i-1] for i in range(1, len(arr))]

# Part 1
def findNext(arr):
    if arr == [0] * len(arr):
        return 0
    else:
        diffs = findDiffs(arr)
        add = findNext(diffs)
        return diffs[-1] + add

# Part 2
def findPrev(arr):
    if arr == [0] * len(arr):
        return 0
    else:
        diffs = findDiffs(arr)
        sub = findPrev(diffs)
        return diffs[0] - sub


totalNext = 0
totalPrev = 0
for sequence in numbers:
    # Part 1
    totalNext += findNext(sequence) + sequence[-1]
    # Part 2
    totalPrev += sequence[0] - findPrev(sequence)

print(totalNext)
print(totalPrev)
