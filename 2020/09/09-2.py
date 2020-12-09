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


def check_part_2(num_to_check: int):
    lowest = 99999999999999
    highest = -1

    test_values = [x for x in values if x < num_to_check]
    print(test_values)
    for start in range(len(test_values)):
        test = 0
        lowest = test_values[start]
        print(f"Testing position {start}: ", end="")
        loop_test_values = test_values[start:]
        for i in range(len(loop_test_values)):
            print(loop_test_values[i], end="+")
            test += loop_test_values[i]

            if loop_test_values[i] > highest:
                highest = loop_test_values[i]

            if test == num_to_check:
                print(f"== {num_to_check}")
                break
            if test > num_to_check:
                # overflow
                print(f"... overflow to {test}")
                break
        if test == num_to_check:
            print(f"{lowest=} {highest=}, combined {lowest+highest}")
            break
        # if the first number + the second number < num_to_check
        # add the next number and check again


for pos in range(preamble, len(values)):
    print(f"Checking line {pos+1} - {values[pos]}")
    last_check = check(values[pos], pos)
    if not last_check:
        print(f"{values[pos]} was not a valid number.")
        check_part_2(values[pos])
        break
