from collections import Counter

FILEPATH = "day1input"
PART = 2

l1, l2 = [], []

with open(FILEPATH) as file:
    for line in file:
        nums = line.split(" ")
        val1, val2 = nums[0], nums[-1]
        l1.append(int(val1))
        l2.append(int(val2))

ans = 0

if PART == 1:
    l1.sort()
    l2.sort()

    for i in range(len(l1)):
        ans += abs(l1[i] - l2[i])
    print(ans)

else:
    # While we could just implement a counter ourselves, for the sake of efficiency...
    c2 = Counter(l2)
    for item in l1:
        ans += c2.get(item, 0) * item
    print(ans)
