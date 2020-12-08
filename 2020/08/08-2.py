with open("2020/08/08.data") as f:
    values = f.read().splitlines()

# Split values
values = [value.split(" ") for value in values]
values = [[x, int(y)] for x, y in values]

accumulator = 0
next_instruction = 0
previous_instruction = 0
visited = list()


def check(inst: str):
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


check(0)

print(f"Accumulator is {accumulator}")

# print(values)
