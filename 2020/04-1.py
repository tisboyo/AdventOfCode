from pydantic.dataclasses import dataclass


@dataclass
class Passport:
    byr: int  # Birth Year
    iyr: int  # Issue Year
    eyr: int  # Expiration Year
    hgt: str  # Height
    hcl: str  # Hair Color
    ecl: str  # Eye Color
    pid: str  # Passport ID
    cid: int = None  # Country ID


with open("2020/04.data") as f:
    values = f.read().splitlines()

# Cleanup data by putting them all in one line
temp_line = ""
new_values = list()
for line in values:
    if line != "":
        temp_line += f" {line}"
    else:
        new_values.append(temp_line)
        temp_line = ""
# There was one line leftover that didn't have a blank line after, so append it too
new_values.append(temp_line)

data_list = list()

for value in new_values:
    # Parse values into a dictionary to be passed to the dataclass for validation
    values_list = value.split()
    value_dict = dict()

    for value in values_list:
        v = value.split(":")
        value_dict[v[0]] = v[1]

    try:
        data_list.append(Passport(**value_dict))
    except TypeError:
        # A value was missing, so invalid passport
        pass


print(len(data_list))
