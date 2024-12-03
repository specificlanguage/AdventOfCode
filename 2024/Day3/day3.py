import re

FILEPATH = "day3input"
PART = 2

with open(FILEPATH) as f:
    inputstr = f.read()

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", inputstr)
ans = 0
enabled = True

# Very simple, stupid python split function
for match in matches:
    if match == 'do()':
        enabled = True
    elif match == "don't()":
        enabled = False
    elif PART == 1 or (PART == 2 and enabled):
        x, y = match[4:-1].split(",")
        x, y = int(x), int(y)
        product = x * y
        ans += product

print(ans)

