import re

f = open("day4/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

scores = {}
count_of_cards = {}
for i in range(1, len(lines) + 1):
    count_of_cards[i] = 1

for i in range(1, len(lines) + 1):
    line = lines[i - 1]
    useful_line = line.split(":")[1]
    question_answer = useful_line.split("|")
    question = question_answer[0]
    answer = question_answer[1]
    winning_numbers = question.strip().split(" ")
    winning_numbers = set([int(number) for number in winning_numbers if number != ""])
    my_numbers = answer.strip().split(" ")
    my_numbers = [int(number) for number in my_numbers if number != ""]
    score = sum([1 for number in my_numbers if number in winning_numbers])
    scores[i] = score
    for j in range(score):
        count_of_cards[i + j + 1] += count_of_cards[i]
print(sum([count_of_cards[i] for i in range(1, len(lines) + 1)]))
