FILEPATH = "day4input"
PART = 2
STR = "XMAS" if PART == 1 else "MAS"
REVERSED = STR[::-1]

grid = []
with open(FILEPATH) as f:
    for line in f:
        grid.append([x for x in line if x != "\n"])

print(grid)
m, n = len(grid), len(grid[0])

def search(x, y):
    ans = 0
    vert = horiz = right_diag = left_diag = ""

    # Vertical answer
    if x < m - 3:
        vert = "".join([grid[i][y] for i in range(x, x+4)])
    # Horizontal answer
    if y < n - 3:
        horiz = "".join([grid[x][i] for i in range(y, y+4)])
    # Right diagonal answer
    if x < m - 3 and y < n - 3:
        right_diag = "".join([grid[x+i][y+i] for i in range(0, 3)])
    # Left diagonal answer
    if x < m - 3 and y >= 3:
        left_diag = "".join([grid[x+i][y-i] for i in range(0, 3)])

    if horiz == STR or horiz == REVERSED:
        print("horiz", x, y, horiz)
        ans += 1
    if vert == STR or vert == REVERSED:
        print("vert", x, y, vert)
        ans += 1
    if left_diag == STR or left_diag == REVERSED:
        print("left_diag", x, y, left_diag)
        ans += 1
    if right_diag == STR or right_diag == REVERSED:
        print("right_diag", x, y, right_diag)
        ans += 1

    if ans > 0:
        print(x, y, ans)
    return ans

def searchX(x, y):
    if x == 0 or x == m -1 or y == 0 or y == n-1: return 0

    left_diag = grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1]
    right_diag = grid[x+1][y-1] + grid[x][y] + grid[x-1][y+1]
    if( left_diag == STR or left_diag == REVERSED) and (right_diag == STR or right_diag == REVERSED):
        return 1
    return 0

total = 0
for i in range(0, m):
    for j in range(0, n):
        if PART == 1:
            total += search(i, j)
        if PART == 2:
            total += searchX(i, j)
print(total)



