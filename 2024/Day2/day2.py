FILEPATH = "day2input"
PART = 2

def isSafe(lst):
    if lst[-1] < lst[0]:  # assume increase
        return isSafeInc(lst, removals=1 if PART > 1 else 0)
    else:
        return isSafeInc(lst[::-1], removals=1 if PART > 1 else 0)

def isSafeInc(lst, removals):
    for i in range(1, len(lst)):
        diff = lst[i-1] - lst[i]
        if lst[i] < lst[i-1] and 1 <= diff <= 3:
            continue
        elif removals > 0:
            # Try removing the previous item
            left = isSafeInc(lst[:i-1] + lst[i:], removals-1)
            # Otherwise try removing yourself
            right = isSafeInc(lst[:i] + lst[i+1:], removals-1)
            return left or right
        else:
            return False
    return True

ans = 0

with open(FILEPATH) as file:
    for line in file:
        lst = [int(x) for x in line.split(" ")]
        res = isSafe(lst)
        print(res, lst)
        ans += 1 if res else 0
    print(ans)
