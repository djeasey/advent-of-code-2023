from tqdm import tqdm
f = open("day16/input.txt", "r")
lines = f.readlines()
lines = [list(line.replace("\n", "")) for line in lines]


def move(current, direction):
    next_point = [current[0], current[1]]
    if direction == "L":
        next_point[1] = current[1] - 1
    elif direction == "R":
        next_point[1] = current[1] + 1
    elif direction == "U":
        next_point[0] = current[0] - 1
    elif direction == "D":
        next_point[0] = current[0] + 1
    if (
        next_point[0] < 0
        or next_point[0] >= len(lines)
        or next_point[1] < 0
        or next_point[1] >= len(lines[0])
    ):
        return []
    if lines[next_point[0]][next_point[1]] == ".":
        return [[next_point, direction]]
    elif lines[next_point[0]][next_point[1]] == "\\":
        if direction == "R":
            return [[next_point, "D"]]
        elif direction == "U":
            return [[next_point, "L"]]
        elif direction == "L":
            return [[next_point, "U"]]
        elif direction == "D":
            return [[next_point, "R"]]
    elif lines[next_point[0]][next_point[1]] == "/":
        if direction == "R":
            return [[next_point, "U"]]
        elif direction == "U":
            return [[next_point, "R"]]
        elif direction == "L":
            return [[next_point, "D"]]
        elif direction == "D":
            return [[next_point, "L"]]
    elif lines[next_point[0]][next_point[1]] == "|":
        if direction in ["U", "D"]:
            return [[next_point, direction]]
        else:
            return [[next_point, "U"], [next_point, "D"]]
    elif lines[next_point[0]][next_point[1]] == "-":
        if direction in ["L", "R"]:
            return [[next_point, direction]]
        else:
            return [[next_point, "L"], [next_point, "R"]]


def num_energised(start_point, start_direction):
    points_visited = move(start_point, start_direction)
    i = 0
    while i < len(points_visited):
        new = move(points_visited[i][0], points_visited[i][1])
        for point in new:
            if point in points_visited:
                continue
            else:
                points_visited.append(point)
        i += 1
    energised_set = set([(point[0][0], point[0][1]) for point in points_visited])
    return len(energised_set)


print("PART 1 ANSWER:")
print(num_energised([0, -1], "R"))
print("PART 2 ANSWER:")
max_energised = 0
for i in tqdm(range(len(lines)), desc="Checking Up/Down"):
    max_energised = max(max_energised,num_energised([-1, i], "D"))
    max_energised = max(max_energised,num_energised([len(lines), i], "U"))
for i in tqdm(range(len(lines[0])), desc="Checking Left/Right"):
    max_energised = max(max_energised,num_energised([i, -1], "R"))
    max_energised = max(max_energised,num_energised([i, len(lines[0])], "L"))
print(max_energised)
