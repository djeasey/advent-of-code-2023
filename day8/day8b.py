from math import lcm

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

# get starting states
starting_states = [x for x in left_moves_dict.keys() if x[2] == "A"]

# get number of moves for each starting state
num_moves = []
for current_state in starting_states:
    i = 0
    while current_state[2] != "Z":
        if moves[i % len(moves)] == "L":
            current_state = left_moves_dict[current_state]
        else:
            current_state = right_moves_dict[current_state]
        i += 1
    num_moves.append(i)

# get the lowest common multiple
print(lcm(*num_moves))
