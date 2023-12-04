import re

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

sum = 0
for line in lines:
    useful_line = line.split(":")[1]
    question_answer = useful_line.split("|")
    question = question_answer[0]
    answer = question_answer[1]
    winning_numbers = question.strip().split(" ")
    winning_numbers = set([int(number) for number in winning_numbers if number != ""])
    my_numbers = answer.strip().split(" ")
    my_numbers = [int(number) for number in my_numbers if number != ""]
    score = 0
    for number in my_numbers:
        if number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score = score * 2
    sum += score
print(sum)
