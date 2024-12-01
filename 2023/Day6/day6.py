FILENAME = "d6input"

with open(FILENAME) as input:
    # Time
    times = input.readline().strip().split(" ")[1:]
    times = "".join([time for time in times if time])
    times = [int(times)]

    # Distances
    distance = input.readline().strip().split(" ")[1:]
    distance = "".join([dist for dist in distance if dist])
    distance = [int(distance)]

    print(times, distance)


def getRecord(time, distance):
    ways = 0
    for i in range(1, time):
        total_dist = i * (time - i)
        if distance < total_dist:
            ways += 1

    return ways

# For part 2, it's technically fast enough that you could do the way below, but I'll also write an optimal way.

answer = 1
for i in range(len(times)):
    answer *= getRecord(times[i], distance[i])
print(answer)


for i in range(times[0]):
    trial = i * (times[0] - i)
    if trial > distance[0]:
        print(trial, times[0] - 2 * i + 1)  # x+1 is needed to count the trial at the end.


