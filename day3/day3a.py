import re

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]


def check_and_sum(lines, i, start_position, end_position, number, sum):
    success = False
    if re.search(
        r"[^A-Za-z0-9\.]",
        lines[i][max(start_position - 1, 0) : min(end_position + 1, len(lines))],
    ):
        sum += number
        success = True
    return sum, success


sum = 0
for i in range(0, len(lines)):
    line = lines[i]
    for match in re.finditer(r"\d+", line):
        start_position = match.start()
        end_position = match.end()
        number = int(line[start_position:end_position])
        success = False
        if i > 0:
            sum, success = check_and_sum(
                lines, i - 1, start_position, end_position, number, sum
            )
        if i < len(lines) - 1 and not success:
            sum, success = check_and_sum(
                lines, i + 1, start_position, end_position, number, sum
            )
        if not success:
            sum, success = check_and_sum(
                lines, i, start_position, end_position, number, sum
            )
print(sum)
