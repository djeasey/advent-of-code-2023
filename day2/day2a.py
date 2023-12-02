f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
sum = 0
for line in lines:
    possible = True
    colon_split_line = line.split(":")
    semicolon_split_line = colon_split_line[1].split(";")
    for i in semicolon_split_line:
        comma_split_line = i.split(",")
        for j in comma_split_line:
            space_split_line = j.split(" ")
            if space_split_line[2] == "red" and int(space_split_line[1]) > 12:
                possible = False
            if space_split_line[2] == "green" and int(space_split_line[1]) > 13:
                possible = False
            if space_split_line[2] == "blue" and int(space_split_line[1]) > 14:
                possible = False
    if possible:
        space_split_line = colon_split_line[0].split(" ")
        sum += int(space_split_line[1])
print(sum)
