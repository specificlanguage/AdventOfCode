from collections import deque

filename = "d10input"
grid = []
startx, starty = -1, -1

right, left, up, down = (0, 1, "-J7"), (0, -1, "-LF"), (-1, 0, "|F7"), (1, 0, "|LJ")

validDirs = {"-": [left, right], "|": [up, down], "L": [up, right], "J": [up, left], "F": [down, right], "7": [down, left]}

with open(filename) as file:
    for line in file:
        grid.append([x for x in line.strip()])
        for j in range(len(line)):
            if line[j] == "S":
                startx, starty = len(grid) - 1, j

m, n = len(grid), len(grid[0])


def getStartingConnections():
    nextNodes = []
    dirs = [left, right, up, down]
    for dx, dy, conns in dirs:
        if grid[startx + dx][starty + dy] in conns and 0 <= startx + dx < m and 0 <= starty + dy < n:
            nextNodes.append((startx + dx, starty + dy, 1))
    return nextNodes

# Part 1 -- it took me a little bit to actually realize the connection matter and i can't do a normal BFS.

def BFS():
    queue = deque(getStartingConnections())
    visited = [[0] * n for _ in range(m)]
    furthest = 0
    while len(queue) > 0:
        x, y, amount = queue.popleft()
        if visited[x][y]:
            continue
        furthest = max(amount, furthest)
        visited[x][y] = amount
        for dx, dy, conns in validDirs[grid[x][y]]:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if not visited[x + dx][y + dy] and \
                        grid[x + dx][y + dy] in conns:
                    # print(x, y, (x + dx, y + dy, amount + 1))
                    queue.append((x + dx, y + dy, amount + 1))
    return furthest, visited

part1, visited = BFS()




print(part1)