f = open("input.txt", "r")
lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

seed_line = lines[0]
seeds = seed_line.split(" ")[1:]
seeds = [int(x) for x in seeds]
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

locations = []
for seed in seeds:
    current_number = seed
    for mapping in mapping_list:
        for chunk in mapping:
            if current_number >= chunk[1] and current_number < chunk[1] + chunk[2]:
                current_number = current_number - chunk[1] + chunk[0]
                break
    locations.append(current_number)
print(min(locations))
