f = open("day14/input.txt", "r")
lines = f.readlines()
lines = [list(line.replace("\n", "")) for line in lines]


def rotate_matrix_90_clockwise(matrix):
    return list(map(list, zip(*matrix[::-1])))


def push_to_right(matrix):
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix[i]) - 1, -1, -1):
            if matrix[i][j] == ".":
                for k in range(j - 1, -1, -1):
                    if matrix[i][k] == "O":
                        matrix[i][j] = "O"
                        matrix[i][k] = "."
                        break
                    elif matrix[i][k] == "#":
                        break
    return matrix


def quarter_turn(matrix):
    matrix = rotate_matrix_90_clockwise(matrix)
    matrix = push_to_right(matrix)
    return matrix


def one_spin(matrix):
    for i in range(4):
        matrix = quarter_turn(matrix)
    return matrix


def load(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                total += j + 1
    return total


print("PART 1 ANSWER:")
print(load(quarter_turn(lines)))

print("PART 2 ANSWER:")
historical_arrays = []
while not any([lines == array for array in historical_arrays[:-1]]):
    lines = one_spin(lines)
    historical_arrays.append(lines)
# get ID where the array repeats
index = historical_arrays.index(lines)
billion_array = historical_arrays[(1000000000 - 1 - index) % (len(historical_arrays) - index - 1) + index]
print(load(rotate_matrix_90_clockwise(billion_array)))
