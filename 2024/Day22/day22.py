import heapq
from collections import defaultdict, deque, Counter
from functools import cache
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

ans = 0

for n in nums:
    secret = n
    for i in range(2000):
        secret = genSecretNumber(secret)
    ans += secret
print(ans)