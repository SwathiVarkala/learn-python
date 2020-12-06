with open('input.txt', 'r') as reader:
    array = reader.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
# numbers = [int(x.strip()) for x in numbers]
# numbers.sort()

array = [x.strip().rstrip('\n') for x in array]

max_seat_id = 0
seats = set()

for row in array:
    start_row, end_row = 0, 127
    start_seat, end_seat = 0, 7
    for i in range(0, 7):
        if row[i] == 'F':
            end_row -= (end_row - start_row + 1)//2
        elif row[i] == 'B':
            start_row += (end_row - start_row + 1) // 2
        # print(i, row[i], start_row, end_row)

    for i in range(7, 10):
        if row[i] == 'L':
            end_seat -= (end_seat - start_seat + 1) // 2
        elif row[i] == 'R':
            start_seat += (end_seat - start_seat + 1) // 2
        # print(i, row[i], start_seat, end_seat)

    current_seat_id = start_row * 8 + start_seat
    seats.add(current_seat_id)
    if current_seat_id > max_seat_id:
        max_seat_id = current_seat_id
print(seats)
last_seat = seats.pop()
for seat in seats:
    if seat - last_seat == 2:
        print(seat - 1)
    last_seat = seat

