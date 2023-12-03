import re

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]


def check_gears(lines, i, start_position, end_position, number, sum, dict_gears):
    for gear in re.finditer(
        r"[\*]",
        lines[i][max(start_position - 1, 0) : min(end_position + 1, len(lines))],
    ):
        if dict_gears.get(
            str(i) + "," + str(gear.start() + max(start_position - 1, 0))
        ):
            sum += (
                number
                * dict_gears[
                    str(i) + "," + str(gear.start() + max(start_position - 1, 0))
                ]
            )
        else:
            dict_gears[
                str(i) + "," + str(gear.start() + max(start_position - 1, 0))
            ] = number
    return sum, dict_gears


sum = 0
dict_gears = {}
for i in range(0, len(lines)):
    line = lines[i]
    for match in re.finditer(r"\d+", line):
        start_position = match.start()
        end_position = match.end()
        number = int(line[start_position:end_position])
        if i > 0:
            sum, dict_gears = check_gears(
                lines, i - 1, start_position, end_position, number, sum, dict_gears
            )
        if i < len(lines) - 1:
            sum, dict_gears = check_gears(
                lines, i + 1, start_position, end_position, number, sum, dict_gears
            )
        sum, dict_gears = check_gears(
            lines, i, start_position, end_position, number, sum, dict_gears
        )
print(sum)
