f = open("day5/input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# Create list of seed ranges
seed_ranges_list = []
seed_line = lines[0]
seeds = seed_line.split(" ")[1:]
for i in range(int(len(seeds) / 2)):
    start = int(seeds[2 * i])
    amount = int(seeds[2 * i + 1])
    seed_ranges_list.append([start, amount])

# Create list of mappings
new_mapping = True
mapping_list = []
mapping = []
for line in lines[2:]:
    if new_mapping:
        mapping = []
        new_mapping = False
    elif line == "":
        new_mapping = True
        mapping_list.append(mapping)
    else:
        new_mapping = False
        line = line.split(" ")
        mapping.append([int(x) for x in line])
mapping_list.append(mapping)

# Start with locations and check if they lead to a valid seed
# Stop when you get a match since we only care about the min location
noneFound = True
while noneFound:
    if i % 1000000 == 0:
        print(i)
    current_number = i
    for mapping in mapping_list[::-1]:
        for chunk in mapping:
            if current_number >= chunk[0] and current_number < chunk[0] + chunk[2]:
                current_number = current_number - chunk[0] + chunk[1]
                break
    for seed_range in seed_ranges_list:
        if (
            current_number >= seed_range[0]
            and current_number < seed_range[0] + seed_range[1]
        ):
            noneFound = False
            break
    i += 1
print(i - 1)
