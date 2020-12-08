from copy import deepcopy

with open("2020/08/08-sample.data") as f:
    values = f.read().splitlines()

# Split values
values = [value.split(" ") for value in values]
values = [[x, int(y)] for x, y in values]

visited = list()


def log_level(message, level):
    for i in range(level):
        print("-", end="")
    print(message)


def check(values: list, inst: str = 0, level: int = 0):
    level += 1
    global accumulator

    if inst in visited:
        # Check if it's a repeat
        return False

    elif inst > len(values):
        return True

    # Record the instructions we've seen
    visited.append(inst)

    if values[inst][0] == "nop":
        log_level("nop", level)
        return check(values, inst + 1, level)

    elif values[inst][0] == "acc":
        log_level(f"acc {values[inst][1]}", level)
        accumulator += values[inst][1]
        return check(values, inst + 1, level)

    elif values[inst][0] == "jmp":
        log_level(f"jmp {values[inst][1]}", level)
        return check(values, inst + values[inst][1], level)


def check1(values: list, inst: int = 0):
    global accumulator
    if inst in visited:
        return False

    visited.append(inst)

    if values[inst][0] == "nop":
        print("nop")
        return check(inst + 1)

    elif values[inst][0] == "acc":
        print("acc", values[inst][1])
        accumulator += values[inst][1]
        return check(inst + 1)

    elif values[inst][0] == "jmp":
        print("jmp", values[inst][1])
        return check(inst + values[inst][1])

    return True


for inst in range(len(values)):
    accumulator = 0
    v = deepcopy(values)
    if values[inst][0] == "nop":
        v[inst][0] = "jmp"
    elif values[inst][0] == "jmp":
        v[inst][0] = "nop"

    result = check1(v)
    if result:
        print(f"Accumulator is {accumulator}")
        break


# print(values)
