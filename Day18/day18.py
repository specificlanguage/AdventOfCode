FILENAME = "d18input"
PART = 2

vertices = [(0, 0, "000000")]
perimeter = 0
direc_map = "RDLU"

with open(FILENAME) as file:
    for line in file:
        sl = line.strip()
        direc, num, colorCode = sl.split(" ")
        curr = [vertices[-1][0], vertices[-1][1]]
        colorCode = colorCode[2:-1]  # Cutoff hashtag and parens

        if PART == 2:
            num = int(colorCode[:-1], 16)
            direc = direc_map[int(colorCode[-1])]

        if direc == "L":
            curr[0] -= int(num)
        if direc == "R":
            curr[0] += int(num)
        if direc == "U":
            curr[1] -= int(num)
        if direc == "D":
            curr[1] += int(num)
        perimeter += int(num)
        vertices.append((curr[0], curr[1], colorCode))

# Shoelace formula

area = 0
for i in range(len(vertices)):
# Calculate the signed area contribution of the current segment and add it to the total area
    area += vertices[i][0] * (vertices[i - 1][1] - vertices[(i + 1) % len(vertices)][1])

area = abs(area) // 2

# Pick's formula to subtract exterior points
interior_points = area - perimeter // 2 + 1
print(interior_points + perimeter)

