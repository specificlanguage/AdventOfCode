import re

FILENAME = "d19input"

workflows = {}
ratings = []
answers = []

def parseWorkflow(line):
    key = line.split("{")[0]
    match = re.search(r"{[:\w,<>]*}", line)
    return {key: match.group(0)}

def workflowResult(workflow, rating):
    # print(workflow, rating)
    match = re.match(r"([xmas][<|>][\d]*):(\w*),(.*)", workflow)
    if match == None: # Is a key
        return workflow
    comparison = match.group(1)
    comp_ok = match.group(2)
    comp_not = match.group(3)

    # print(comparison, comp_ok, comp_not)
    valToCompare = rating[comparison[0]]

    if comparison[1] == "<":
        if valToCompare < int(comparison[2:]):
            return comp_ok
        else:
            return workflowResult(comp_not, rating)
    elif comparison[1] == ">":
        if valToCompare > int(comparison[2:]):
            return comp_ok
        else:
            return workflowResult(comp_not, rating)


with open(FILENAME) as file:
    isRatings = False
    for line in file:
        if line.strip() == "":
            isRatings = True
            continue
        if isRatings:
            ratings.append({x[0]: int(x[2:]) for x in line.strip()[1:-1].split(",")})
        else:
            workflows.update(parseWorkflow(line.strip()))

for rating in ratings:
    key = "in"
    while key not in ["R", "A"]:
        workflow = workflows[key]
        key = workflowResult(workflow[1:-1], rating)
        # print("next key:", key)
    if key == "A":
        answers.append(rating)

# print(answers)
print(sum([sum(answers[i].values()) for i in range(len(answers))]))

