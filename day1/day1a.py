import re

f = open("input.txt", "r")
lines = f.readlines()
print(sum([int(re.search(rf"\d", line).group() + re.search(rf"\d", line).group()) for line in lines]))
