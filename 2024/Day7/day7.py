from math import ceil, floor, log10

FILENAME = "day7input"
PART = 2

ans = 0

def solve(result, nums):

    def solve_rec(result, curr, nums):
        if len(nums) == 0:
            if curr == result:
                return True
            return False

        prod, sum = curr * nums[0], curr + nums[0]

        if prod <= result:     # Continue
            isValid = solve_rec(result, prod, nums[1:])
            if isValid:
                return True
        if sum <= result:
            isValid = solve_rec(result, sum, nums[1:])
            if isValid:
                return True

        if PART == 2:
            concat = int(str(curr) + str(nums[0]))
            if concat <= result:
                # print(curr, "->", concat, ", left to go: ", nums[1:])
                isValid = solve_rec(result, concat, nums[1:])
                if isValid:
                    return True

        return False

    curr = nums[0]
    return solve_rec(result, curr, nums[1:])

with open(FILENAME) as f:
    for line in f:
        line = line.strip()
        result, nums = line.split(":")
        result = int(result)
        nums = [int(n) for n in nums.strip().split()]

        if solve(result, nums):
            ans += result

print(ans)
