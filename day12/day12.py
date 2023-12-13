from functools import cache
f = open("day12/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

@cache
def rec_fun(arr = tuple, groups = tuple, current_size = int):
    if len(groups) == 0: # no more groups left. only valid if arr is entirely . or ?
        if arr.count("#") == 0: return 1
        else: return 0
    elif len(arr) == 0: # no more arr left. only valid if groups is entirely 0
        if len(groups) == 0 and current_size == 0: return 1
        elif len(groups) == 1 and groups[0] == current_size: return 1
        else: return 0
    elif arr[0] == "#":
        if current_size > groups[0]: return 0
        else: return rec_fun(arr[1:], groups, current_size + 1)
    elif arr[0] == ".":
        if current_size == 0: return rec_fun(arr[1:], groups, 0)
        elif current_size == groups[0]: return rec_fun(arr[1:], groups[1:], 0)
        else: return 0
    else: # arr[0] == "?"
        if current_size == groups[0]: return rec_fun(arr[1:], groups[1:], 0)
        elif current_size > groups[0]: return 0
        elif current_size == 0: return rec_fun(arr[1:], groups, 0) + rec_fun(arr[1:], groups, 1)
        else: return rec_fun(arr[1:], groups, current_size + 1)

print("PART 1 ANSWER:")
print(sum([rec_fun(tuple(line.split(" ")[0]), tuple([int(x) for x in line.split(" ")[1].split(",")]), 0) for line in lines]))
print("PART 2 ANSWER:")
print(sum([rec_fun(tuple('?'.join([line.split(" ")[0]] * 5)), tuple([int(x) for x in line.split(" ")[1].split(",") * 5]), 0) for line in lines]))
