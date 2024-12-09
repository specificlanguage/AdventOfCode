# Basic idea is to go for a basic two pointers solution. Nothing crazy, until it blows up in our face.

FILEPATH = 'day9test'

memory = []

with open(FILEPATH) as f:
    inputstr = f.read()

start_ptr = 0
for i in range(len(inputstr)):
    if i % 2 == 0: # Piece of memory
        memory.extend([i // 2] * int(inputstr[i]))
    else:
        memory.extend([-1] * int(inputstr[i]))

left, right = 0, len(memory)-1

while True:
    # Find next free piece of memory
    while left < right and memory[left] != -1:
        left += 1
        # print(left)
    # Find next allocated piece of memory
    while left < right and memory[right] == -1:
        right -= 1
        # print(right)
    if left >= right:
        # print(left, right)
        break
    else:
        memory[left], memory[right] = memory[right], memory[left]
        # print(left, right)

ans = 0
for i in range(len(memory)):
    if memory[i] == -1:
        break
    ans += memory[i] * i
print(ans)


