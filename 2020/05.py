from collections import namedtuple


nt = namedtuple("Seat", "row col id")


def get_seat_id(seats: str):
    rows = range(127)
    cols = range(7)

    for seat in seats:
        current_length_row = len(rows)
        current_length_col = len(cols)
        if seat == "F":
            split_on = current_length_row // 2  # Lower half
            rows = rows[:split_on]
        elif seat == "B":
            split_on = current_length_row // 2 + 1  # Higher half
            rows = rows[split_on:]
        elif seat == "L":  # Lower half
            split_on = current_length_col // 2
            cols = cols[:split_on]
        elif seat == "R":
            split_on = current_length_col // 2 + 1  # Higher half
            cols = cols[split_on:]

    return nt(rows.start, cols.start, (rows.start * 8 + cols.start))


# print(get_seat_id("FBFBBFFRLR"))  # Seat(row=44, col=5, id=357)
# print(get_seat_id("BFFFBBFRRR"))  # Seat(row=70, col=7, id=567)
# print(get_seat_id("FFFBBBFRRR"))  # Seat(row=14, col=7, id=119)
# print(get_seat_id("BBFFBBFRLL"))  # Seat(row=102, col=4, id=820)

with open("2020/05.data") as f:
    values = f.read().splitlines()

nt_list = list()
for value in values:
    nt_list.append(get_seat_id(value))

sorted_list_of_seats = sorted(nt_list, key=lambda x: x.id)
print(f"Highest Seat ID: {sorted_list_of_seats[-1]}")

unaccounted_for_seats = set(
    range(sorted_list_of_seats[0].id, sorted_list_of_seats[-1].id)
)
for seat in sorted_list_of_seats:
    if seat.id in unaccounted_for_seats:
        unaccounted_for_seats.remove(seat.id)

print(f"Your seat: {unaccounted_for_seats}")
