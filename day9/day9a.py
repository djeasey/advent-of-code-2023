f = open("day9/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

sum = 0
for line in lines:
    diff_list = []
    diff_list.append([int(x) for x in line.split()])

    # create difference pyramid
    while set(diff_list[-1]) != set([0]):
        new_differences = []
        for i in range(len(diff_list[-1]) - 1):
            new_differences.append(diff_list[-1][i + 1] - diff_list[-1][i])
        diff_list.append(new_differences)

    # predict the next value as the sum of the last numbers in each list
    predicted_value = 0
    for list in diff_list:
        predicted_value += list[-1]
    sum += predicted_value

print(sum)
