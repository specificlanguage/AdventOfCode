from collections import deque

FILEPATH = 'day10input'

lines = []

with open(FILEPATH) as f:
    for line in f:
        l = line.strip()
        lines.append([x for x in l])

ans = 0
starting_points = []
m, n = len(lines), len(lines[0])

# Search for starting points, aka 0s
for r in range(m):
    for c in range(n):
        if lines[r][c] == '0':
            starting_points.append((r, c))

# Let's start searching!
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def calcTrails(stp):

    queue = deque([stp])
    tops = set()

    while queue:
        r, c, step = queue.popleft()

        # Just add to solution if at top.
        if step == 9:
            if (r, c) not in tops:
                tops.add((r, c))
            continue
        for dr, dc in directions:
            if 0 <= r + dr < m and 0 <= c + dc < n:
                # print(r + dr, c + dc, lines[r + dr][c + dc], str(step + 1))
                if lines[r + dr][c + dc] == str(step + 1):
                    queue.append((r + dr, c + dc, step + 1))

    return len(tops)

for sp in [(s[0], s[1], 0) for s in starting_points]:
    num_tops = calcTrails(sp)
    ans += num_tops

print(ans)

