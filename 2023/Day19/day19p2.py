import re
import math
from copy import deepcopy
from collections import deque

FILENAME = "d19input"

class Range:
    def __init__(self, low, high):
        self.low, self.high = low, high

    def splitHigh(self, x: int):
        return Range(x, self.high)

    def splitLow(self, x: int):
        return Range(self.low, x)

    def getRange(self):
        return self.high - self.low + 1

def parseWorkflow(line):
    key = line.split("{")[0]
    match = re.search(r"{[:\w,<>]*}", line)
    return {key: match.group(0)}

def workflowResult(workflow, ranges: dict[Range]):

    nextItems = []
    # print(workflow, rating)
    match = re.match(r"([xmas][<|>][\d]*):(\w*),(.*)", workflow)

    if match == None:  # Is a key
        return nextItems
    comparison = match.group(1)
    comp_ok = match.group(2)
    comp_not = match.group(3)

    if comparison[1] == "<":
        compKey, val = comparison[0], int(comparison[2:])

        invalidRange = dict(ranges)
        invalidRange[compKey] = ranges[compKey].splitHigh(val)
        ranges[compKey] = ranges[compKey].splitLow(val)

        nextItems.append((ranges, comp_ok))
        nextItems += workflowResult(comp_not, invalidRange)

    elif comparison[1] == ">":
        compKey, val = comparison[0], int(comparison[2:])

        invalidRange = dict(ranges)
        invalidRange[compKey] = ranges[compKey].splitLow(val)
        ranges[compKey] = ranges[compKey].splitHigh(val)
        print(invalidRange == ranges)

        nextItems.append((ranges, comp_ok))
        nextItems += workflowResult(comp_not, invalidRange)

    return nextItems

workflows = {}

with open(FILENAME) as file:
    isRatings = False
    for line in file:
        if line.strip() == "":
            isRatings = True
            continue
        if isRatings:
            break  # no need to worry about it for part 2
        else:
            workflows.update(parseWorkflow(line.strip()))

items = deque([({k: Range(1, 4000) for k in "xmas"}, "in")])
accepted = []
while len(items) > 0:
    r, key = items.popleft()
    print(key)
    if key == "A":  # Accepted
        accepted.append(r)
        continue
    if key == "R":  # Rejected
        continue
    items += workflowResult(workflows[key][1:-1], r)
    print(len(accepted), len(items))

print([[(x.low, x.high) for x in accepted[i].values()] for i in range(len(accepted))])
print(sum([math.prod([x.getRange() for x in accepted[i].values()]) for i in range(len(accepted))]))

