from collections import defaultdict

FILENAME = "day8input"
PART = 1

ans = 0
grid = []

with open(FILENAME) as f:
    for line in f:
        line = [x for x in line.strip()]
        grid.append(line)

m, n = len(grid), len(grid[0])
antennae = defaultdict(list)

# Load antenna types
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != ".":
            antennae[grid[r][c]].append((r, c))

answers = set()

def antinodeCalculations(tower1, tower2): # Tower 1 is (x, y), # Tower 2 is (a, b)
    # Find the slope between towers 1 and 2.
    x1, y1 = tower1[0], tower1[1]
    x2, y2 = tower2[0], tower2[1]

    # Use precalculated things to find antinodes via point slope formula
    # New location = 2x1 - x2,
    x_dist = x2 - x1
    y_dist = y2 - y1

    valid_points = []

    if PART == 1:
        return [
            (x1 - x_dist, y1 - y_dist),
            (x2 + x_dist, y2 + y_dist),
        ]

    # Look before first, check if still in bounds.
    queue = [(x1, y1)]
    visited = set()
    while len(queue) > 0:
        # print(queue)
        x, y = queue.pop()
        if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
            valid_points.append((x, y))
            visited.add((x, y))
            queue.append((x + x_dist, y + y_dist))
            queue.append((x - x_dist, y - y_dist))

    # Original code, above is a different version. Below does work, I just decided to clean
    # this up when I was committing.
    #
    # poss_x, poss_y = (x1 - i * (x_dist), y1 - i * (y_dist))
    # if 0 <= poss_x < m and 0 <= poss_y < n:
    #     valid_points.append((poss_x, poss_y))
    #     i += 1
    # else:
    #     break

    # i = 0
    # while True or (i == 1 and PART == 1):
    #     poss_x, poss_y = (x2 + i * (x_dist), y2 + i * (y_dist))
    #     if 0 <= poss_x < m and 0 <= poss_y < n:
    #         valid_points.append((poss_x, poss_y))
    #         i += 1
    #     else:
    #         break

    return valid_points

for at in antennae:
    at_list = antennae[at]
    for i in range(len(at_list)):
        for j in range(i+1, len(at_list)):
            tower1, tower2 = at_list[i], at_list[j]
            # print(tower1, tower2)
            locs = antinodeCalculations(tower1, tower2)

            if PART == 1:
                for x, y in locs:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in answers:
                        answers.add((x, y))

            elif PART == 2:
                for x, y in locs:
                    if (x, y) not in answers:
                        answers.add((x, y))

# print(sorted(answers))
print(len(answers))