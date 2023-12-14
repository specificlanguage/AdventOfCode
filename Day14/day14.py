import copy

FILENAME = "d14input"

lines = []

for line in open(FILENAME):
    lines.append([c for c in line.strip()])

def rot_90(matrix):  # 90 counter clockwise
    height = len(matrix)
    length = len(matrix[0])
    new_matrix = []

    for x in range(0,length):
        line = [matrix[y][x] for y in range(0, height)]
        line.reverse()
        new_matrix.append(line)

    return new_matrix

def find_new_slide_y_north(matrix, curr_y, x):
    for test_y in range(curr_y, -1, -1):
        if matrix[test_y-1][x] == 'O' or matrix[test_y-1][x] == '#':
            return test_y
    return 0

def rollGrid(matrix):
    for y in range(1, len(matrix)):
        for x in range(0, len(matrix[0])):
            if (matrix[y][x] == 'O'):
                new_y = find_new_slide_y_north(matrix, y, x)
                if y != new_y:
                    matrix[y][x] = '.'
                    matrix[new_y][x] = 'O'

    return matrix

def countWeight(line):
    totalWeight = 0
    currWeight = len(line)
    for i, c in enumerate(line):
        if c == "#":
            currWeight = len(line) - i - 1
        elif c == "O":
            totalWeight += currWeight
            currWeight -= 1
    return totalWeight

# Flipping for easier work, starts with north facing left
lines = list(map(list, zip(*lines)))
curr = [[c for c in line] for line in lines]
old_grids = []

for i in range(0, 1000000000):
    curr = rollGrid(curr)
    curr = rot_90(curr)
    curr = rollGrid(curr)
    curr = rot_90(curr)
    curr = rollGrid(curr)
    curr = rot_90(curr)
    curr = rollGrid(curr)
    curr = rot_90(curr)

    if not curr in old_grids:
        old_grids.append(copy.deepcopy(curr))
    else:
        # Found period
        break

# Math to find period
beforePeriod = old_grids.index(curr)
period = i - beforePeriod
goal_i = 1000000000
i_1000000000 = (goal_i - beforePeriod) % period + beforePeriod - 1
matrix = old_grids[i_1000000000]

result = 0
for y in range(0, len(matrix)):
    for x in range(0, len(matrix[0])):
        if matrix[y][x] == 'O':
            result += len(matrix) - y
print(result)
print(matrix)

