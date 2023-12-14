from functools import cache
f = open("day12/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# this recursive function calculates the number of possible arrangements
# given an tuple of ., ?, and # and a tuple of group sizes
@cache
def count_valid_arrangements(springs = tuple, groups = tuple, current_size = int):
    if len(groups) == 0: # no more groups left to make
        if springs.count("#") == 0: return 1 # only valid if remaining springs is entirely . or ?
        else: return 0 # hashes left with no groups to put them in so invalid
    elif len(springs) == 0: # no more springs left
        if len(groups) == 1 and groups[0] == current_size: return 1 # final group is the right size so valid endpoint
        else: return 0 # final group is wrong size so invalid
    elif current_size > groups[0]: return 0 # current group is too big so invalid
    elif springs[0] == "#": return count_valid_arrangements(springs[1:], groups, current_size + 1) # keep building the current group
    elif springs[0] == ".":
        if current_size == 0: return count_valid_arrangements(springs[1:], groups, 0) # back-to-back . so keep going
        elif current_size == groups[0]: return count_valid_arrangements(springs[1:], groups[1:], 0) # finished a group and reset current_size
        else: return 0 # group ended early so invalid
    else: # springs[0] == "?"
        if current_size == groups[0]: return count_valid_arrangements(springs[1:], groups[1:], 0) # finished a group and reset current_size. ? must be a .
        elif current_size == 0: return count_valid_arrangements(springs[1:], groups, 0) + count_valid_arrangements(springs[1:], groups, 1) # ? can be a . OR a #
        else: return count_valid_arrangements(springs[1:], groups, current_size + 1) # 0 < current_size < groups[0] so ? can only be a #

print("PART 1 ANSWER:")
print(sum([count_valid_arrangements(tuple(line.split(" ")[0]), tuple([int(x) for x in line.split(" ")[1].split(",")]), 0) for line in lines]))
print("PART 2 ANSWER:")
print(sum([count_valid_arrangements(tuple('?'.join([line.split(" ")[0]] * 5)), tuple([int(x) for x in line.split(" ")[1].split(",") * 5]), 0) for line in lines]))
