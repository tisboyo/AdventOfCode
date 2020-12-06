with open("2020/06.data") as f:
    values = f.read().splitlines()

# Cleanup data by putting them all in one line
temp_line = ""
new_values = list()
people = 0
for line in values:

    if line != "":
        temp_line += f"{line}"
        people += 1
    else:
        new_values.append((temp_line, people))
        people = 0
        temp_line = ""
# There was one line leftover that didn't have a blank line after, so append it too
new_values.append((temp_line, people))


total_yes_count = 0
for line in new_values:
    s = set(line[0])
    for letter in s:
        if line[0].count(letter) == line[1]:
            total_yes_count += 1

print(total_yes_count)
