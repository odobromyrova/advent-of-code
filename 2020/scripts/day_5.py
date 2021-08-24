from utils import get_filepath_from_command_line


def get_seat_row_info(seating_record, n_row_indicating_chars, total_row_number):
    row_list = [i for i in range(total_row_number)]
    mid_point = int(total_row_number / 2)

    for char in seating_record[:n_row_indicating_chars]:
        if char == 'F':
            row_list = row_list[:mid_point]
            mid_point = int(len(row_list) / 2)

        if char == 'B':
            row_list = row_list[mid_point:]
            mid_point = int(len(row_list) / 2)

    return row_list[0]


def get_seat_number_info(seating_record, n_seat_indicating_chars, total_seats_number):
    seat_list = [i for i in range(total_seats_number)]
    mid_point = int(total_seats_number / 2)

    for char in seating_record[n_seat_indicating_chars:]:
        if char == 'L':
            seat_list = seat_list[:mid_point]
            mid_point = int(len(seat_list) / 2)

        if char == 'R':
            seat_list = seat_list[mid_point:]
            mid_point = int(len(seat_list) / 2)

    return seat_list[0]


def create_seat_ids_set(seating_data):
    seat_id_set = set()

    for seating_record in seating_data:
        row_id = get_seat_row_info(seating_record, 7, 128)
        seat_id = get_seat_number_info(seating_record, 3, 8)
        unique_seat_id = row_id * 8 + seat_id
        seat_id_set.add(unique_seat_id)

    return seat_id_set


def find_missing_seat_id(seat_id_set):
    seat_list = list(seat_id_set)
    seat_list = sorted(seat_list)

    for i in range(len(seat_list)):
        if seat_list[i + 1] - seat_list[i] == 2:
            missing_value = seat_list[i] + 1
            break

    return missing_value


def run(seating_info_file):
    with open(seating_info_file, "r+") as file:
        seating_data = [line.replace('\n', '') for line in file.readlines()]

    seat_id_set = create_seat_ids_set(seating_data)

    part_1_result = max(seat_id_set)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't identify highest seat ID.")

    part_2_result = find_missing_seat_id(seat_id_set)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't find missing seat ID.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
