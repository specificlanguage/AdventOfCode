import heapq

FILENAME = "d11input"

grid = []
galaxyLocations = []
emptyRows = []
emptyCols = []

# Setup information
with open(FILENAME) as file:
    for i, line in enumerate(file):
        line = line.strip()
        for j in range(len(line)):
            if line[j] == "#":
                galaxyLocations.append((i, j))
        grid.append(line)

def emptyColumn(c):
    isEmpty = True
    for i in range(len(grid)):
        if grid[i][c] != ".":
            return False
    return True

m, n = len(grid), len(grid[0])

emptyRows = [r for r in range(len(grid)) if grid[r] == "." * len(grid[0])]
emptyCols = [c for c in range(len(grid)) if emptyColumn(c)]
dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def djikstra(srcX, srcY, goals):
    if not goals:
        return []
    h = [(0, srcX, srcY)]
    destinations = []
    visited = [[False] * n for _ in range(m)]
    while h:
        dist, i, j = heapq.heappop(h)
        if visited[i][j]:
            continue

        visited[i][j] = True
        if (i, j) in goals:
            destinations.append(dist)
            if len(destinations) == len(goals):
                return destinations

        for x, y in dirs:
            if 0 <= i + x < m and 0 <= j + y < n and not visited[i+x][j+y]:
                # PLease note: Part 2 is literally just changing this
                travel = 1000000 if i+x in emptyRows or j+y in emptyCols else 1
                heapq.heappush(h, (travel + dist, i+x, j+y))

    return destinations

total = 0
print("Found {0} galaxies".format(len(galaxyLocations)))
for i in range(len(galaxyLocations)): # Don't waste an extra cycle on something I don't need
    x, y = galaxyLocations[i]
    total += sum(djikstra(x, y, galaxyLocations[i+1:]))
    print("Completed galaxy " + str(i))
print(total)