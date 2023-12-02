f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
sum = 0
for line in lines:
    min_red = 0
    min_green = 0
    min_blue = 0
    colon_split_line = line.split(":")
    semicolon_split_line = colon_split_line[1].split(";")
    for i in semicolon_split_line:
        comma_split_line = i.split(",")
        for j in comma_split_line:
            space_split_line = j.split(" ")
            if space_split_line[2] == "red" and int(space_split_line[1]) > min_red:
                min_red = int(space_split_line[1])
            if space_split_line[2] == "green" and int(space_split_line[1]) > min_green:
                min_green = int(space_split_line[1])
            if space_split_line[2] == "blue" and int(space_split_line[1]) > min_blue:
                min_blue = int(space_split_line[1])
    sum += min_red * min_green * min_blue
print(sum)
