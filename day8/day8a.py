f = open("day8/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
lines = [line.replace(" ", "") for line in lines]
lines = [line.replace("(", "") for line in lines]
lines = [line.replace(")", "") for line in lines]
moves = lines[0]

# create moves dicts
left_moves_dict = {}
right_moves_dict = {}
for line in lines[2:]:
    move = line.split("=")
    left_moves_dict[move[0]] = move[1].split(",")[0]
    right_moves_dict[move[0]] = move[1].split(",")[1]

# calculate number of moves from AAA to ZZZ
current_state = "AAA"
i = 0
while current_state != "ZZZ":
    if moves[i % len(moves)] == "L":
        current_state = left_moves_dict[current_state]
    else:
        current_state = right_moves_dict[current_state]
    i += 1

print(i)
