import heapq
from collections import defaultdict, deque, Counter
from functools import cache
import itertools
from math import log10, floor, isclose, lcm
import re

FILEPATH = 'day23input'
graph = defaultdict(list)

with open(FILEPATH) as f:
    for line in f:
        n1, n2 = line.strip().split("-")
        graph[n1].append(n2)
        graph[n2].append(n1)

# Finding a clique of a fixed size. Fun!
def findConnectedGraphSize3(node):
    queue = deque([(node, [node])])
    sets = set()
    while queue:
        curr, path = queue.popleft()
        if len(path) > 4: # No need to see it anymore
            continue
        if len(path) == 4 and path[0] == path[-1]:
            sets.add(tuple(sorted(path[:-1])))
        else:
            neighbors = graph[curr]
            for n in neighbors:
                queue.append((n, path + [n]))
    return sets

three_sets = set()
for node in graph:
    sets = findConnectedGraphSize3(node)
    three_sets = three_sets.union(sets)

t_sets = 0
for x, y, z, in three_sets:
    if x[0] == 't' or y[0] == 't' or z[0] == 't':
        t_sets += 1
print(t_sets)
