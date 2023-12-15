import re

f = open("day15/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
line = lines[0].split(",")


def hash_alg(string):
    current = 0
    for char in string:
        # determine ascii code for char
        current += ord(char)
        current *= 17
        current = current % 256
    return current


print("PART 1 ANSWER:")
print(sum([hash_alg(string) for string in line]))

print("PART 2 ANSWER:")
boxes = [[] for i in range(256)]

for string in line:
    split_string = re.split("=|-", string)
    label = split_string[0]
    box_number = hash_alg(label)
    if "=" in string:
        focal_len = int(split_string[1])
        try:
            index = [box[0] for box in boxes[box_number]].index(label)
            boxes[box_number][index][1] = focal_len
        except ValueError:
            boxes[box_number].append([label, focal_len])
    else:
        try:
            index = [box[0] for box in boxes[box_number]].index(label)
            boxes[box_number] = (
                boxes[box_number][:index] + boxes[box_number][index + 1 :]
            )
        except ValueError:
            pass

total = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        total += (i + 1) * (j + 1) * boxes[i][j][1]
print(total)
