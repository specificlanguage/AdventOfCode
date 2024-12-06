from collections import defaultdict, deque, Counter

FILENAME = "day6input"
PART = 2

grid = []
row_blockers = defaultdict(list)
col_blockers = defaultdict(list)
currRow, currCol = 0, 0

with open(FILENAME) as f:
    for line in f:
        grid.append([c for c in line.strip()])

# Find start locations
for i in range(len(grid)):
    for j in range(len(grid[0])):
            if grid[i][j] == "^":
                currRow, currCol = i, j

m, n = len(grid), len(grid[0])
print(m, n)

def ans(startR, startC):

    currRow, currCol = startR, startC
    num_spaces = 1
    visited = set()
    cached_calls = set()

    def goUp(r, c) -> (int, int, int): # nx, ny, num_spaces, end
        traveled = 0
        while True:
            if r - 1 == -1 or grid[r-1][c] == "#":
                return r, c, traveled
            else:
                traveled += 1
                r -= 1
                visited.add((r, c))

    def goDown(r, c) -> (int, int, int): # nx, ny, num_spaces, end
        traveled = 0
        while True:
            if r + 1 == m or grid[r+1][c] == "#":
                return r, c, traveled
            else:
                traveled += 1
                r += 1
                visited.add((r, c))

    def goLeft(r, c) -> (int, int, int):
        traveled = 0
        while True:
            if c - 1 == -1 or grid[r][c-1] == "#":
                return r, c, traveled
            else:
                traveled += 1
                c -= 1
                visited.add((r, c))

    def goRight(r, c) -> (int, int, int):
        traveled = 0
        while True:
            if c + 1 == n or grid[r][c+1] == "#":
                return r, c, traveled
            else:
                traveled += 1
                c += 1
                if r == startR and c == startC and PART == 2:
                    return r, c, traveled
                visited.add((r, c))

    visited.add((currRow, currCol))

    while True:
        ops = [goUp, goRight, goDown, goLeft]
        for op in ops:

            if (currRow, currCol, op) in cached_calls and PART == 2:
                return 1
            newRow, newCol, traveled = op(currRow, currCol)
            cached_calls.add((currRow, currCol, op))

            num_spaces += traveled
            # print(currRow, currCol, "to", newRow, newCol, "traveled", traveled, "total", num_spaces)
            if 0 == newRow or m - 1 == newRow or 0 == newCol or n - 1 == newCol:
                if PART == 2:
                    return 0
                return len(visited)
            else:
                currRow, currCol = newRow, newCol

if PART == 1:
    print(ans(currRow, currCol))

if PART == 2:
    total = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != "#":
                grid[i][j] = "#"
                total += ans(currRow, currCol)
                grid[i][j] = "."
    print(total)
