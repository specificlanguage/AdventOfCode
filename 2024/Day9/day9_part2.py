# Basic idea is to go for a basic two pointers solution. Nothing crazy, until it blows up in our face.
# Well, it did blow up in our face huh.

from heapq import heappush, heappop

FILEPATH = 'day9input'
free_blocks = [] # Form of {start: end}
allocated_blocks = {} # Form of (id: (start, length))

with open(FILEPATH) as f:
    inputstr = f.read()

start_ptr = 0
for i in range(len(inputstr)):
    if i % 2 == 0: # Piece of memory
        allocated_blocks[i // 2] = (start_ptr, int(inputstr[i]))
    else:
        free_blocks.append((start_ptr, start_ptr + int(inputstr[i])))
    start_ptr += int(inputstr[i])

blocks_to_replace = sorted(allocated_blocks.keys())

while blocks_to_replace:
    block = blocks_to_replace.pop()
    _, length_needed = allocated_blocks[block]
    sel_location = -1

    push_back = []

    # Find free blocks
    while free_blocks:
        start, end = heappop(free_blocks)
        if start > allocated_blocks[block][0]: # No need to look anymore left
            break
        if end - start >= length_needed:
            # Replace the old free block, free the allocated block
            new_start, new_end = start + length_needed, end
            if new_end - new_start > 0:
                heappush(free_blocks, (new_start, new_end))
            # Move the allocated block
            allocated_blocks[block] = start, length_needed
            break
        else:
            push_back.append((start, end))

    for x in push_back:
        heappush(free_blocks, x)

    # print(free_blocks)
    # print(allocated_blocks)

ans = 0
for id in allocated_blocks:
    start, length = allocated_blocks[id]
    for i in range(length):
        ans += id * (start + i)

print(ans)
