import heapq
from collections import defaultdict, deque, Counter
from functools import cache
import itertools
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day22input'
lines = []

with open(FILEPATH) as f:
    nums = [int(l) for l in f.read().split("\n")]

def mix(m, n):
    return m ^ n

def prune(m):
    return m % 16777216

@cache
def genSecretNumber(prev_secret):
    # Step 1
    s1 = prune(mix(prev_secret, prev_secret * 64))
    # Step 2
    s2 = prune(mix(s1, s1 // 32))
    # Step 3
    s3 = prune(mix(s2, s2 * 2048))
    return s3

# One partial strategy is to pre-generate the possible price changes, making 20P4 possibilities.
# We can then do a basic check to make sure we actually get a profit.

def generateChangePermutations():
    possible_changes = list(range(-9, 10))
    valid_permutations = defaultdict(int)
    all_perms = list(itertools.product(possible_changes, repeat=4))
    for perm in all_perms:
        valid_permutations[perm] = 0
    return valid_permutations

def addChanges(prices, change_perms):
    price_queue = deque([])
    seen = set()
    for p1, p2 in itertools.pairwise(prices): # Generate the price diffs for the first four.
        price_queue.append(p2 - p1)
        if len(price_queue) > 4:
            price_queue.popleft()
        if len(price_queue) == 4:
            seq = tuple(price_queue)
            if seq not in seen:
                change_perms[tuple(price_queue)] += p2
                seen.add(seq)

ans = 0
perms = generateChangePermutations()

for n in nums:
    secret = n
    prices = [secret % 10]
    for i in range(2000):
        secret = genSecretNumber(secret)
        prices.append(secret % 10)
    addChanges(prices, perms)

# print("-----")

# Show the price max that was best
best_perm = max(perms, key=perms.get)
print(best_perm)
print(perms[best_perm])

# print(perms[(-2,1,-1,3)])