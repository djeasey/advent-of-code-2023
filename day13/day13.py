from copy import deepcopy

f = open("day13/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# get list of list of lists set up
patterns = []
pattern = []
for i in range(len(lines)):
    if lines[i] == "":
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(list(lines[i]))
patterns.append(pattern)


# given a pattern this function returns the score of the reflection unless it is equal to ignore
def get_reflection_score(pattern, ignore=0):
    # check for horizontal reflection
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:
            # potential candidate
            failed_reflection = False
            for j in range(min(len(pattern[: i + 1]), len(pattern[i + 1 :]))):
                if pattern[i - j] != pattern[i + 1 + j]:
                    failed_reflection = True
            if not failed_reflection:
                score = (i + 1) * 100
                if score != ignore:  # ignore the original reflection
                    return score
    # check for vertical reflection
    for i in range(len(pattern[0]) - 1):
        if [pattern[j][i] for j in range(len(pattern))] == [
            pattern[j][i + 1] for j in range(len(pattern))
        ]:
            # potential candidate
            failed_reflection = False
            for j in range(min(len(pattern[0][: i + 1]), len(pattern[0][i + 1 :]))):
                if [pattern[k][i - j] for k in range(len(pattern))] != [
                    pattern[k][i + 1 + j] for k in range(len(pattern))
                ]:
                    failed_reflection = True
            if not failed_reflection:
                score = i + 1
                if score != ignore:  # ignore the original reflection
                    return score
    return 0


total_a = 0
total_b = 0
for x in range(len(patterns)):
    pattern_no_change = patterns[x]
    original_score = get_reflection_score(pattern_no_change)
    total_a += original_score
    # try every symbol swap and check for new reflections
    for i in range(len(pattern_no_change)):
        for j in range(len(pattern_no_change[i])):
            new_pattern = deepcopy(pattern_no_change)
            if new_pattern[i][j] == "#":
                new_pattern[i][j] = "."
            else:
                new_pattern[i][j] = "#"
            score = get_reflection_score(new_pattern, original_score)
            total_b += score

print("PART 1 ANSWER:")
print(total_a)
print("PART 2 ANSWER:")
print(int(total_b / 2))  # each reflection is counted twice
