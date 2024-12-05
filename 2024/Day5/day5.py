from collections import defaultdict

FILEPATH = "day5input"
PART = 2
SECTION = 1

before = defaultdict(set)
ans = 0

def checkValidList(nums):
    printed = set([nums[0]])
    for i in range(1, len(nums)):
        # Get all nums y needed to be printed before x
        reqs = before[nums[i]]
        # print(nums[i], reqs)
        for req in reqs:
            if req in printed:
                return False
        printed.add(nums[i])
    return True

def rearrange(nums) -> list[int]:
    # Rearrange the list to be before a certain item.
    new_list = [nums[0]]

    for i in range(1, len(nums)):
        reqs = before[nums[i]]
        insertEnd = True

        for j in range(0, i): # Items in the new list
            if new_list[j] in reqs: # Always insert before earliest item in the list.
                print(nums[i], nums[j], reqs)
                new_list = new_list[:j] + [nums[i]] + new_list[j:]
                insertEnd = False
                break
        if insertEnd:
            new_list.append(nums[i])

    return new_list


with open(FILEPATH) as f:
    # f.readlines()
    for line in f:
        line = line[:-1] # prune new line, i'm dumb
        # print(line)
        if line == "":
            SECTION += 1
            continue

        if SECTION == 1:
            # print(line.split("|"))
            x, y = line.split("|")
            before[int(x)].add(int(y)) # In this case, x must be printed before y

        elif SECTION == 2:
            nums = [int(x) for x in line.split(",")]
            # print(nums)
            # We can generally assume all books have odd amount of pages
            is_valid = checkValidList(nums)
            if is_valid and PART == 1:
                # print(nums, len(nums))
                middle = nums[len(nums) // 2]
                ans += middle
            elif not is_valid and PART == 2:
                print(nums, rearrange(nums))
                nums = rearrange(nums)
                middle = nums[len(nums) // 2]
                ans += middle

            # print("-----")


print(ans)