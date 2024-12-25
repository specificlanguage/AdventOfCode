import heapq
from collections import defaultdict, deque, Counter
from functools import cache
import itertools
from math import log10, floor, isclose, lcm
import random
import re

FILEPATH = 'day23input'
graph = defaultdict(list)

with open(FILEPATH) as f:
    for line in f:
        n1, n2 = line.strip().split("-")
        graph[n1].append(n2)
        graph[n2].append(n1)

# Finding a clique of a maximum size. Fun!
ans = defaultdict(set)
def bronKerbosch(R, P, X):
    if len(P) == 0 and len(X) == 0:
        ans[len(R)].add(tuple(sorted(R)))
        return
    u = P.union(X).pop()
    for v in P.difference(set(graph[u])):
        bronKerbosch(R.union([v]), P.intersection(graph[v]), X.intersection(graph[v]))
        P = P.difference(v)
        X = X.union(v)

bronKerbosch(set(), set(graph.keys()), set())
max_size = max(ans)
max_tuple = ans[max_size]
print(max_tuple)
print(",".join(list(max_tuple)[0]))
