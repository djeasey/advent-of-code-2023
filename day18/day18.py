f = open("day18/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]


def next_point(current_pos, direction, steps, area, perim):
    if direction in ("R", "0"): dx, dy = 0, steps
    elif direction in ("L", "2"): dx, dy = 0, -1 * steps
    elif direction in ("U", "3"): dx, dy = -1 * steps, 0
    elif direction in ("D", "1"): dx, dy = steps, 0
    area += (2 * current_pos[1] + dy) * dx  # part of shoelace formula
    new_pos = [current_pos[0] + dx, current_pos[1] + dy]
    perim += steps
    return new_pos, area, perim


print("PART 1 ANSWER:")
current_pos, area, perim = [0, 0], 0, 0
for line in lines:
    current_pos, area, perim = next_point(current_pos, line.split()[0], int(line.split()[1]), area, perim)
print(perim // 2 + area // 2 + 1)  # https://en.wikipedia.org/wiki/Shoelace_formula

print("PART 2 ANSWER:")
current_pos, area, perim = [0, 0], 0, 0
for line in lines:
    current_pos, area, perim = next_point(current_pos, line.split()[2][7], int(line.split()[2][2:7], 16), area, perim)
print(perim // 2 + area // 2 + 1)  # https://en.wikipedia.org/wiki/Shoelace_formula
