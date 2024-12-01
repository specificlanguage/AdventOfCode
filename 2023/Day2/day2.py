FILENAME = "d2input.txt"

MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14
total = 0
prodtotal = 0

for line in open(FILENAME):
    game, draws = line.split(":")
    C = {}
    for draw in draws.split(";"):
        for ball in draw.split(","):
            number, color = ball.split()
            C[color] = max(C.get(color, 0), int(number))
    if C["red"] <= MAX_RED and C["green"] <= MAX_GREEN and C["blue"] <= MAX_BLUE:
        total += int(game.split()[1])
    prodtotal += C["red"] * C["green"] * C["blue"]
print(total)
print(prodtotal)
