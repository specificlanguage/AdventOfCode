import re

with open("d4input.txt") as f:
    lines = f.read().split("\n")

totalPts = 0
cardCopies = [1] * len(lines)

for i, line in enumerate(lines):
    cardScore = 0
    ticketList = line.split("|")
    ticket = [int(n) for n in re.findall(r"\d+", ticketList[0])[1:]]
    winning = set(int(n) for n in re.findall(r"\d+", ticketList[1]))
    wins = 0
    nextCopies = 0
    for number in ticket:
        if number in winning:
            nextCopies += 1
            if wins == 0:
                wins += 1
            else:
                wins *= 2
    totalPts += wins

    # PART 2
    if i < len(cardCopies) - 1:
        # Distribute to the next parts of the list
        copiesToAdd = [nextCopies // (len(cardCopies) - i - 1)] * (len(cardCopies) - i - 1)
        extra = nextCopies - len(cardCopies) * copiesToAdd[0]
        for j in range(extra):
            copiesToAdd[j] += 1
            extra -= 1

        # Multiply by amount of copies of the current ticket
        copiesToAdd = list(map(lambda x: x * cardCopies[i], copiesToAdd))
        # print(copiesToAdd)

        for j in range(len(copiesToAdd)):
            cardCopies[i + j + 1] += copiesToAdd[j]

    # print(cardCopies)

# PART 1
print(totalPts)

# PART 2

print(sum(cardCopies))
# print(cardCopies)