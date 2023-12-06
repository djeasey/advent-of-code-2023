f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# Remove spaces to get time and distance
time = int(lines[0].replace(" ","").split(":")[1])
distance_goal = int(lines[1].replace(" ","").split(":")[1])

# Loop over hold times and see how many result in a win
print(len([1 for hold_time in range(time+1) if distance_goal < (time - hold_time) * hold_time]))
