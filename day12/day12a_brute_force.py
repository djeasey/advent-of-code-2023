import itertools
from copy import deepcopy

f = open("day12/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]


def is_string_valid(input=str, grouping=list):
    input = input.replace(".", " ")
    input_array = input.split()
    lengths = [len(x) for x in input_array]
    return lengths == grouping


total = 0
for line in lines:
    split_line = line.split(" ")
    input = split_line[0]
    grouping = [int(x) for x in split_line[1].split(",")]
    num_damaged = sum(grouping)
    num_known = input.count("#")
    num_unknown = num_damaged - num_known
    if num_unknown == 0:
        sub_total = 1
    else:
        num_questions = input.count("?")
        question_indices = [i for i, char in enumerate(input) if char == "?"]
        all_combs = [
            list(comb) for comb in itertools.combinations(question_indices, num_unknown)
        ]

        sub_total = 0
        for comb in all_combs:
            new_input = deepcopy(input)
            for i in comb:
                new_input = new_input[:i] + "#" + new_input[i + 1 :]
                new_input = new_input.replace("?", ".")

            if is_string_valid(new_input, grouping):
                sub_total += 1
    total += sub_total

print(total)
