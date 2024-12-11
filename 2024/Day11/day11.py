from math import log10, floor

FILEPATH = 'day11input'

stones = []

with open(FILEPATH) as f:
    stones = [int(n) for n in f.read().strip().split(' ')]

# Well, I guess we follow the rules huh
calc_cache = {0: [1]}
solve_cache = {} # form of
# Isn't caching fun?

def blink(num):
    if calc_cache.get(num):
        return calc_cache[num]
    log = floor(log10(num))
    if log % 2 == 1:  # 10^3 = 1000, 4 digits, so it works.
        div = 10 ** (log // 2 + 1)
        n1, n2 = num // div, num % div
        calc_cache[num] = [n1, n2]
        return [n1, n2]
    else:
        mult = num * 2024
        calc_cache[num] = [mult]
        return [mult]

# You basically just want to take it one 'input' at a time, but then also cache the result.

def solve(nums, i):
    tup = tuple(nums)
    if (i, tup) in solve_cache:
        return solve_cache[(i, tup)]
    if i == 0:
        solve_cache[(i, tup)] = len(nums)
        return len(nums)
    else:
        res = sum(solve(blink(num), i-1) for num in nums)
        solve_cache[(i, tup)] = res
        return res

print(solve(stones, 75))