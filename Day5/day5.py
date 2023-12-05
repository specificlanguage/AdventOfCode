from collections import deque

FILENAME = "d5input"

lines = []
seeds = []
maps = []
with open(FILENAME) as f:
    str_seeds = f.readline().strip().split(" ")[1:]

    for i in range(len(str_seeds) // 2):
        start, length = str_seeds[i * 2], str_seeds[i * 2 + 1]
        # print(start, length)
        seeds.append(range(int(start), int(start) + int(length)))

    for line in f:
        if line == "\n":
            maps.append({})
        elif line[0].isalpha():  # maps header
            continue
        else:
            [dest, src, length] = line.strip().split(" ")
            maps[-1][int(src)] = (int(dest), int(length))

sources = deque(seeds)
for map in maps:
    nextSources = deque([])
    visited = set()

    # print(sources, map)

    for src in map:  # Map each source to their destination in each map
        dest, length = map[src]
        overflow = deque([])
        while len(sources) > 0:
            seedRange = sources.popleft()

            # Check for overlap fit
            matchStart, matchEnd = max(seedRange.start, src), min(seedRange.stop, src + length)

            if matchEnd - matchStart > 0:

                if seedRange.start < matchStart:
                    overflow.append(range(seedRange.start, matchStart - 1))
                if matchEnd < seedRange.stop:
                    overflow.append(range(matchEnd, seedRange.stop))

                destStart, destEnd = matchStart - src + dest, matchEnd - src + dest
                # print(src, length, seedRange, matchStart, matchEnd, destStart, destEnd)
                nextSources.append(range(destStart, destEnd))

            else:
                overflow.append(seedRange)

        sources = overflow

    sources = nextSources + overflow

    # print("-------------")


min_start = float("inf")
for source in sources:
    min_start = min(source.start, min_start)
print(min_start)

