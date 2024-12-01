from collections import deque

FILENAME = "d16input"
PART = 2

grid = []

for line in open(FILENAME):
    grid.append([c for c in line.strip()])

m, n = len(grid), len(grid[0])

def getTilesEnergized(startr, startc, direct):
    visited = []
    visited_tiles = []
    queue = deque([(startr, startc, direct)])

    while len(queue) > 0:
        r, c, direction = queue.popleft()
        # print(r, c, direction)

        if (r, c, direction) in visited:
            continue
        else:
            visited.append((r, c, direction))
            if (r, c) not in visited_tiles:
                visited_tiles.append((r, c))

        # Look at all this direction fiddling!
        if grid[r][c] == "/":
            if direction == "r" and 0 <= r - 1:
                queue.append((r - 1, c, "u"))
            elif direction == "u" and c + 1 < n:
                queue.append((r, c + 1, "r"))
            elif direction == "d" and 0 <= c - 1:
                queue.append((r, c - 1, "l"))
            elif direction == "l" and r + 1 < m:
                queue.append((r + 1, c, "d"))

        elif grid[r][c] == "\\":
            if direction == "r" and r + 1 < m:
                queue.append((r + 1, c, "d"))
            elif direction == "u" and 0 <= c - 1:
                queue.append((r, c - 1, "l"))
            elif direction == "d" and c + 1 < n:
                queue.append((r, c + 1, "r"))
            elif direction == "l" and 0 <= r - 1:
                queue.append((r - 1, c, "u"))

        elif grid[r][c] == "-":
            if direction == "r" and c + 1 < n:
                queue.append((r, c + 1, "r"))
            elif direction == "l" and 0 <= c - 1:
                queue.append((r, c - 1, "l"))
            elif direction == "u" or direction == "d":
                if 0 <= c - 1:
                    queue.append((r, c - 1, "l"))
                if c + 1 < n:
                    queue.append((r, c + 1, "r"))

        elif grid[r][c] == "|":
            if direction == "r" or direction == "l":
                if 0 <= r - 1:
                    queue.append((r - 1, c, "u"))
                if r + 1 < m:
                    queue.append((r + 1, c, "d"))
            elif direction == "u" and 0 <= r - 1:
                queue.append((r - 1, c, "u"))
            elif direction == "d" and r + 1 < m:
                queue.append((r + 1, c, "d"))

        elif direction == "r" and c + 1 < n:
            queue.append((r, c + 1, "r"))
        elif direction == "l" and 0 <= c - 1:
            queue.append((r, c - 1, "l"))
        elif direction == "u" and 0 <= r - 1:
            queue.append((r - 1, c, "u"))
        elif direction == "d" and r + 1 < m:
            queue.append((r + 1, c, "d"))

    return len(visited_tiles)


if PART == 1:
    print(getTilesEnergized(0, 0, "r"))

if PART == 2:
    maxTiles = 0
    # What happened is that I accidentally reversed the coordinates in the wrong direction, but at least I'm consistent!
    for i in range(m):
        maxTiles = max(maxTiles, getTilesEnergized(i, 0, "r"))
        maxTiles = max(maxTiles, getTilesEnergized(i, n-1, "c"))
        print(f"Completed row {i}, maxTiles: {maxTiles}")
    for i in range(n):
        maxTiles = max(maxTiles, getTilesEnergized(0, i, "d"))
        maxTiles = max(maxTiles, getTilesEnergized(m-1, i, "u"))
        print(f"Completed column {i}, maxTiles: {maxTiles}")

    print(maxTiles)
