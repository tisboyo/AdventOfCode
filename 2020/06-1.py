with open("2020/06.data") as f:
    values = f.read().splitlines()

# Cleanup data by putting them all in one line
temp_line = ""
new_values = list()
for line in values:
    if line != "":
        temp_line += f"{line}"
    else:
        new_values.append(temp_line)
        temp_line = ""
# There was one line leftover that didn't have a blank line after, so append it too
new_values.append(temp_line)

total_yes_count = 0
for line in new_values:
    new_set = set()
    for letter in line:
        if letter not in new_set:
            new_set.add(letter)

    total_yes_count += len(new_set)

print(total_yes_count)
