f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# Create a time list and a distance list
times = lines[0].split(" ")
times = [int(time) for time in times[1:] if time != ""]
distances = lines[1].split(" ")
distances = [int(distance) for distance in distances[1:] if distance != ""]

# Loop over races and see how many hold times result in a win
product = 1
for race in range(len(times)):
    sum = 0
    for hold_time in range(times[race]+1):
        release_time = times[race] - hold_time
        distance = release_time * hold_time
        if distances[race] < distance:
            sum += 1
    product *= sum

print(product)