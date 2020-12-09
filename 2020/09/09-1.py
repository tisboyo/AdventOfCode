from itertools import combinations

preamble = 25

with open("2020/09/09.data", "r") as f:
    # sample data is a preamble of 5, live is 25
    values = f.read().splitlines()

# Convert all of the numbers to actual numbers
values = [int(x) for x in values]


def check(num_to_check: int, start_position: int):
    start = start_position - preamble
    stop = preamble + start
    v = values[start:stop]
    pairs = combinations(v, 2)
    for test_nums in pairs:
        if test_nums[0] + test_nums[1] == num_to_check:
            return test_nums

    else:
        return False


for pos in range(preamble, len(values)):
    print(f"Checking line {pos+1} - {values[pos]}")
    last_check = check(values[pos], pos)
    if not last_check:
        print(f"{values[pos]} was not a valid number.")
        break

    # maths = a[0] + a[1] if a is not False else 0
    # # print(a, maths, values[pos])
