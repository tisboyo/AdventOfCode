with open("2020/08/08.data") as f:
    values = f.read().splitlines()

# Split values
values = [value.split(" ") for value in values]
values = [[x, int(y)] for x, y in values]

accumulator = 0
next_instruction = 0
visited = list()
while True:
    current_instruction = next_instruction
    if next_instruction in visited:
        break
    elif values[next_instruction][0] == "nop":
        print("nop")
        next_instruction += 1
    elif values[next_instruction][0] == "acc":
        print("acc")
        accumulator += values[next_instruction][1]
        next_instruction += 1
    elif values[next_instruction][0] == "jmp":
        print("jmp")
        next_instruction += values[next_instruction][1]
    else:
        "Error Will Robinson!"

    # Add the current instruction to the check for dupe
    visited.append(current_instruction)
    blah = None

print(f"Fault! Accumulator is {accumulator}")

# print(values)
