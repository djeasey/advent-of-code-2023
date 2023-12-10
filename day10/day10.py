f = open("day10/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# Find the start location "S"
for i in range(len(lines)):
    if "S" in lines[i]:
        start = [i, lines[i].index("S")]
        break

valid_pipe_paths = []


def move(path, direction):
    if direction == "E":
        return path + [[path[-1][0], path[-1][1] + 1]]
    elif direction == "W":
        return path + [[path[-1][0], path[-1][1] - 1]]
    elif direction == "N":
        return path + [[path[-1][0] - 1, path[-1][1]]]
    elif direction == "S":
        return path + [[path[-1][0] + 1, path[-1][1]]]


def current_symbol(path):
    return lines[path[-1][0]][path[-1][1]]


# traverse the grid in each direction until you hit a dead end or return to the start
for latest_direction in ("E", "S", "W", "N"):
    path = [start]
    path = move(path, latest_direction)
    while True:
        if latest_direction == "E":
            if current_symbol(path) == "-":
                latest_direction = "E"
            elif current_symbol(path) == "7":
                latest_direction = "S"
            elif current_symbol(path) == "J":
                latest_direction = "N"
            else:
                latest_direction = "X"
        elif latest_direction == "S":
            if current_symbol(path) == "J":
                latest_direction = "W"
            elif current_symbol(path) == "L":
                latest_direction = "E"
            elif current_symbol(path) == "|":
                latest_direction = "S"
            else:
                latest_direction = "X"
        elif latest_direction == "W":
            if current_symbol(path) == "L":
                latest_direction = "N"
            elif current_symbol(path) == "F":
                latest_direction = "S"
            elif current_symbol(path) == "-":
                latest_direction = "W"
            else:
                latest_direction = "X"
        elif latest_direction == "N":
            if current_symbol(path) == "7":
                latest_direction = "W"
            elif current_symbol(path) == "F":
                latest_direction = "E"
            elif current_symbol(path) == "|":
                latest_direction = "N"
            else:
                latest_direction = "X"
        if latest_direction == "X":
            break
        path = move(path, latest_direction)
    if current_symbol(path) == "S":
        valid_pipe_paths.append(path)

path = valid_pipe_paths[0]

print("PART 1 ANSWER:")
print(int((len(path) - 1) / 2))

# create a copy that only includes the valid path
new_grid = [["." for i in range(len(lines[0]))] for j in range(len(lines))]
for i in range(len(path)):
    new_grid[path[i][0]][path[i][1]] = lines[path[i][0]][path[i][1]]

# use the even-ness of the count of |JLS to the left of each empty space to determine if it is trapped
count_trapped = 0
for i in range(len(new_grid)):
    for j in range(len(new_grid[0])):
        if new_grid[i][j] == ".":
            count_left = 0
            for k in range(j):
                if new_grid[i][k] in "|JLS":
                    count_left += 1
            if count_left % 2 == 1:
                count_trapped += 1
                new_grid[i][j] = "I"

print("PART 2 ANSWER:")
print(count_trapped)
