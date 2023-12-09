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

    # predict the previous value as the alternating sum of the first numbers in each list
    predicted_value = 0
    for i in range(len(diff_list)):
        if i % 2 == 0:
            predicted_value += diff_list[i][0]
        else:
            predicted_value -= diff_list[i][0]
    sum += predicted_value

print(sum)
