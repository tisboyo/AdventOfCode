from pydantic.dataclasses import dataclass
from re import match


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

    def validate_height(self):
        value = int(self.hgt[:-2])

        if self.hgt[-2:] == "cm":
            ret = True if 150 <= value <= 193 else False
        elif self.hgt[-2:] == "in":
            ret = True if 59 <= value <= 76 else False
        else:
            raise TypeError

        return ret

    def validate(self):
        if (
            (1920 <= int(self.byr) <= 2002)
            and (2010 <= int(self.iyr) <= 2020)
            and (2020 <= int(self.eyr) <= 2030)
            and (self.validate_height())
            and (match("^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", self.hcl))
            and (self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            and (len(self.pid) == 9 and self.pid.isnumeric())
        ):
            return True

    def __post_init__(self):
        if not self.validate():
            raise TypeError


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
