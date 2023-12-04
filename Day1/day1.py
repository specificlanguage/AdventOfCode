numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

def getFirstAndLastNumber(line: str):
    first = last = None
    for i in range(len(line)):
        if line[i].isnumeric():
            if first is None:
                first = int(line[i])
            last = int(line[i])
        else:
            for key in numbers:
                if line[i-len(key)+1:i+1] == key:
                    # print(line[i-len(key)+1:i+1])
                    if first is None:
                        first = numbers[key]
                    last = numbers[key]

    return first * 10 + last

with open("d1input.txt") as file:
    sum = 0
    for line in file:
        num = getFirstAndLastNumber(line)
        sum += num
    print(sum)