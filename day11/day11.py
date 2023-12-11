f = open("day11/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# find the empty rows and columns
empty_rows = []
for i in range(len(lines)):
    if set(lines[i]) == set("."):
        empty_rows.append(i)
empty_columns = []
for j in range(len(lines[0])):
    if set([lines[x][j] for x in range(len(lines))]) == set("."):
        empty_columns.append(j)

# find the galaxies
galaxies = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            galaxies.append([i, j])

# find the total distance between each pair of galaxies
total_distance_a = 0
total_distance_b = 0
for i in range(len(galaxies)):
    for j in range(len(galaxies)):
        if i < j:
            num_empty_rows = len(
                [
                    x
                    for x in empty_rows
                    if galaxies[i][0] < x < galaxies[j][0]
                    or galaxies[j][0] < x < galaxies[i][0]
                ]
            )
            num_empty_cols = len(
                [
                    x
                    for x in empty_columns
                    if galaxies[i][1] < x < galaxies[j][1]
                    or galaxies[j][1] < x < galaxies[i][1]
                ]
            )
            distance_a = (
                abs(galaxies[i][0] - galaxies[j][0])
                + num_empty_rows
                + abs(galaxies[i][1] - galaxies[j][1])
                + num_empty_cols
            )
            total_distance_a += distance_a
            multiplier = 1000000 - 1
            distance_b = (
                abs(galaxies[i][0] - galaxies[j][0])
                + multiplier * num_empty_rows
                + abs(galaxies[i][1] - galaxies[j][1])
                + multiplier * num_empty_cols
            )
            total_distance_b += distance_b

print("PART 1 ANSWER:")
print(total_distance_a)
print("PART 2 ANSWER:")
print(total_distance_b)
