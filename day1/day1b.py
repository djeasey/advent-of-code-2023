import re
from word2number import w2n

f = open("day1/input.txt", "r")
lines = f.readlines()
sum = 0
for line in lines:
    number_strings = "one|two|three|four|five|six|seven|eight|nine"
    first_number_string = re.search(rf"\d|{number_strings}", line).group()
    first_number = w2n.word_to_num(first_number_string)
    second_number_string = re.search(rf"\d|{number_strings[::-1]}", line[::-1]).group()[::-1]
    second_number = w2n.word_to_num(second_number_string)
    sum += int(str(first_number) + str(second_number))
print(sum)
