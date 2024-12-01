FILENAME = "d15input"
PART = 2

with open(FILENAME) as f:
    seq = f.readline().strip()
    codes = seq.split(",")

# both parts
def hashCode(seq):
    val = 0
    for char in seq:
        val += ord(char)
        val *= 17
        val %= 256
    return val

# Part 2 only
def findIndexInBucket(lst, item):
    for i in range(len(lst)):
        if lst[i][:len(item)] == item:
            return i
    return -1

def replaceInBucket(lst, item, num: str):
    for i in range(len(lst)):
        if lst[i][:len(item)] == item:
            lst[i] = item + num
            return
    lst.append(item + num)


if PART == 1:
    total = 0
    for code in codes:
        total += hashCode(code)
    print(total)

else:
    buckets = [[] for _ in range(256)]
    for code in codes:
        if code[-1] == "-":
            bucketNum = hashCode(code[:-1])
            bucket = buckets[bucketNum]
            ind = findIndexInBucket(bucket, code[:-1])
            if ind >= 0:
                bucket.pop(ind)

        elif code[-2] == "=":
            bucket = hashCode(code[:-2])
            replaceInBucket(buckets[bucket], code[:-2], code[-1])

    total = 0
    # print(buckets)
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            # print((i+1), (j+1), int(buckets[i][j][-1]), (i + 1) * (j+1) * int(buckets[i][j][-1]))
            total += (i + 1) * (j+1) * int(buckets[i][j][-1])
    print(total)

