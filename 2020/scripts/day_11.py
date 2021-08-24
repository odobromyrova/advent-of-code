from copy import deepcopy
from utils import get_filepath_from_command_line


def identify_seats_with_many_occ_adj(ferry_data):
    seats_to_replace = []

    for line_id, line in enumerate(ferry_data):
        for seat_id, seat in enumerate(line):
            count_occ_seats = 0
            list_to_check = []
            prev_line = []
            current_line = []
            next_line = []
            if seat == '.':
                continue

            # Handling first seat in the row
            if seat_id == 0:
                if line_id == 0:
                    current_line = list(ferry_data[line_id][seat_id + 1])
                    next_line = list(ferry_data[line_id + 1][:  seat_id + 2])

                elif line_id == len(ferry_data) - 1:
                    prev_line = list(ferry_data[line_id - 1][: seat_id + 2])
                    current_line = list(ferry_data[line_id][seat_id + 1])

                else:
                    prev_line = list(ferry_data[line_id - 1][: seat_id + 2])
                    current_line = list(ferry_data[line_id][seat_id + 1])
                    next_line = list(ferry_data[line_id + 1][:  seat_id + 2])

            # Handling Last seat in the row
            elif seat_id == len(line) - 1:
                if line_id == 0:
                    current_line = list(ferry_data[line_id][seat_id - 1])
                    next_line = list(ferry_data[line_id + 1][seat_id - 1:])

                elif line_id == len(ferry_data) - 1:
                    prev_line = list(ferry_data[line_id - 1][seat_id - 1:])
                    current_line = list(ferry_data[line_id][seat_id - 1])

                else:
                    prev_line = list(ferry_data[line_id - 1][seat_id - 1:])
                    current_line = list(ferry_data[line_id][seat_id - 1])
                    next_line = list(ferry_data[line_id + 1][seat_id - 1:])

            # Handling Middle seats in the row
            else:
                if line_id == 0:
                    current_line = list(ferry_data[line_id][seat_id - 1] + ferry_data[line_id][seat_id + 1])
                    next_line = list(ferry_data[line_id + 1][seat_id - 1:  seat_id + 2])

                elif line_id == len(ferry_data) - 1:
                    prev_line = list(ferry_data[line_id - 1][seat_id - 1: seat_id + 2])
                    current_line = list(ferry_data[line_id][seat_id - 1] + ferry_data[line_id][seat_id + 1])

                else:
                    prev_line = list(ferry_data[line_id - 1][seat_id - 1: seat_id + 2])
                    current_line = list(ferry_data[line_id][seat_id - 1] + ferry_data[line_id][seat_id + 1])
                    next_line = list(ferry_data[line_id + 1][seat_id - 1:  seat_id + 2])

            string_to_check = list(prev_line + current_line + next_line)

            count_occ_seats += sum([x == '#' for x in string_to_check])

            if count_occ_seats >= 4:
                seats_to_replace.append([line_id, seat_id])

    return seats_to_replace


def identify_seats_to_occupy(ferry_data):
    seats_to_replace = []

    for line_id, line in enumerate(ferry_data):
        for seat_id, seat in enumerate(line):
            count_occ_seats = 0
            list_to_check = []
            prev_line = []
            current_line = []
            next_line = []
            if seat not in ['.', '#']:

                # Handling first seat in the row
                if seat_id == 0:
                    if line_id == 0:
                        current_line = list(ferry_data[line_id][seat_id + 1])
                        next_line = list(ferry_data[line_id + 1][:  seat_id + 2])

                    elif line_id == len(ferry_data) - 1:
                        prev_line = list(ferry_data[line_id - 1][: seat_id + 2])
                        current_line = list(ferry_data[line_id][seat_id + 1])

                    else:
                        prev_line = list(ferry_data[line_id - 1][: seat_id + 2])
                        current_line = list(ferry_data[line_id][seat_id + 1])
                        next_line = list(ferry_data[line_id + 1][:  seat_id + 2])

                # Handling Last seat in the row
                elif seat_id == len(line) - 1:
                    if line_id == 0:
                        current_line = list(ferry_data[line_id][seat_id - 1])
                        next_line = list(ferry_data[line_id + 1][seat_id - 1:])

                    elif line_id == len(ferry_data) - 1:
                        prev_line = list(ferry_data[line_id - 1][seat_id - 1:])
                        current_line = list(ferry_data[line_id][seat_id - 1])

                    else:
                        prev_line = list(ferry_data[line_id - 1][seat_id - 1:])
                        current_line = list(ferry_data[line_id][seat_id - 1])
                        next_line = list(ferry_data[line_id + 1][seat_id - 1:])


                # Handling Middle seats in the row
                else:
                    if line_id == 0:
                        current_line = list(ferry_data[line_id][seat_id - 1] + ferry_data[line_id][seat_id + 1])
                        next_line = list(ferry_data[line_id + 1][seat_id - 1:  seat_id + 2])

                    elif line_id == len(ferry_data) - 1:
                        prev_line = list(ferry_data[line_id - 1][seat_id - 1: seat_id + 2])
                        current_line = list(ferry_data[line_id][seat_id - 1] + ferry_data[line_id][seat_id + 1])

                    else:
                        prev_line = list(ferry_data[line_id - 1][seat_id - 1: seat_id + 2])
                        current_line = list(ferry_data[line_id][seat_id - 1] + ferry_data[line_id][seat_id + 1])
                        next_line = list(ferry_data[line_id + 1][seat_id - 1:  seat_id + 2])

                string_to_check = list(prev_line + current_line + next_line)

                count_occ_seats += sum([x == '#' for x in string_to_check])

                if count_occ_seats == 0:
                    seats_to_replace.append([line_id, seat_id])

    return seats_to_replace


def find_new_seating_state(ferry_data):
    new_state = deepcopy(ferry_data)

    seats_to_replace = identify_seats_with_many_occ_adj(ferry_data)
    for record in seats_to_replace:
        new_state[record[0]][record[1]] = 'L'

    seats_to_replace = identify_seats_to_occupy(ferry_data)
    for record in seats_to_replace:
        new_state[record[0]][record[1]] = '#'

    return new_state


def find_final_occ_seats_count(ferry_data):
    previous_state = ferry_data
    current_state = None

    while True:
        current_state = find_new_seating_state(previous_state)

        if current_state == previous_state:
            break

        previous_state = current_state

    occupied_seats = sum(letter == '#' for line in current_state for letter in line)
    return occupied_seats


#Part 2
def calculate_occ_seats_to_the_left(seat_id, line, seat_counter):
    for seat_id_iter in range(seat_id - 1, -1, -1):
                if line[seat_id_iter] == 'L':
                    break
                elif line[seat_id_iter] == '#':
                    seat_counter += 1
                    break
    return seat_counter


def calculate_occ_seats_to_the_right(seat_id, line, seat_counter):
    for seat_id_iter in range(seat_id + 1, len(line)):
        if line[seat_id_iter] == 'L':
            break
        elif line[seat_id_iter] == '#':
            seat_counter += 1
            break

    return seat_counter


def calculate_occ_seats_to_the_north(seat_id, line_id, test_data, seat_counter):
    for line_id_iter in range(line_id - 1, -1, -1):
        if test_data[line_id_iter][seat_id] == 'L':
            break
        elif test_data[line_id_iter][seat_id] == '#':
            seat_counter += 1
            break
    return seat_counter


def calculate_occ_seats_to_the_south(seat_id, line_id, test_data, seat_counter):
    for line_id_iter in range(line_id + 1, len(test_data)):
        if test_data[line_id_iter][seat_id] == 'L':
            break
        elif test_data[line_id_iter][seat_id] == '#':
            seat_counter += 1
            break

    return seat_counter


def calculate_occ_seats_in_the_upper_diagonal(seat_id, line_id, test_data, seat_counter, direction='left'):
    for line_id_iter in range(line_id - 1, -1, -1):
        if direction == 'left':
            line_id_change = line_id - line_id_iter
        else:
            line_id_change = - (line_id - line_id_iter)

        if (seat_id - line_id_change >= 0) and (seat_id - line_id_change < len(test_data[line_id_iter])):
            if test_data[line_id_iter][seat_id - line_id_change] == 'L':
                break
            elif test_data[line_id_iter][seat_id - line_id_change] == '#':
                seat_counter += 1
                break
    return seat_counter


def calculate_occ_seats_in_the_lower_diagonal(seat_id, line_id, test_data, seat_counter, direction='left'):
    for line_id_iter in range(line_id + 1, len(test_data)):
        if direction == 'left':
            line_id_change = line_id_iter - line_id
        else:
            line_id_change = - (line_id_iter - line_id)

        if (seat_id - line_id_change >= 0) and (seat_id - line_id_change < len(test_data[line_id_iter])):
            if test_data[line_id_iter][seat_id - line_id_change] == 'L':
                break
            elif test_data[line_id_iter][seat_id - line_id_change] == '#':
                seat_counter += 1
                break

    return seat_counter


def identify_visibly_occupied_seats(test_data, number_of_occupied_seats=5, goal='freeup'):
    seats_to_change_list = []

    if goal == 'freeup':
        seat_pattern = '#'
    elif goal == 'occupy':
        seat_pattern = 'L'
    else:
        raise ValueError('Goal value {} is not supported'.format(goal))

    for line_id, line in enumerate(test_data):
        for seat_id, seat in enumerate(line):
            seat_counter = 0

            if seat != seat_pattern:
                continue

            # Occupied seats horizontally
            if seat_id != 0:
                # get everything on the left horizontally
                seat_counter = calculate_occ_seats_to_the_left(seat_id, line, seat_counter)

            if seat_id != len(line) - 1:
                # get everything on the right horizontally
                seat_counter = calculate_occ_seats_to_the_right(seat_id, line, seat_counter)

            # Occupied seats higher vertically

            if line_id != 0:
                # get everything to the north
                seat_counter = calculate_occ_seats_to_the_north(seat_id, line_id, test_data, seat_counter)

            if line_id != len(test_data) - 1:
                # get everything to the south
                seat_counter = calculate_occ_seats_to_the_south(seat_id, line_id, test_data, seat_counter)

            # Occupied seats diagonally
            if line_id != 0:
                if seat_id != len(line) - 1:
                    # get everything occupied in the upper right diagonal
                    seat_counter = calculate_occ_seats_in_the_upper_diagonal(seat_id, line_id,
                                                                             test_data, seat_counter,
                                                                             direction='right')

                if seat_id != 0:
                    # get everything occupied in the upper left diagonal
                    seat_counter = calculate_occ_seats_in_the_upper_diagonal(seat_id, line_id,
                                                                             test_data, seat_counter,
                                                                             direction='left')

            if line != len(test_data) - 1:
                if seat_id != 0:
                    # get everything occupied in the lower left diagonal
                    seat_counter = calculate_occ_seats_in_the_lower_diagonal(seat_id, line_id,
                                                                             test_data, seat_counter,
                                                                             direction='left')

                if seat_id != len(line) - 1:
                    # get everything occupied in the lower right diagonal
                    seat_counter = calculate_occ_seats_in_the_lower_diagonal(seat_id, line_id,
                                                                             test_data, seat_counter,
                                                                             direction='right')

            if goal == 'freeup':
                if seat_counter >= number_of_occupied_seats:
                    seats_to_change_list.append([line_id, seat_id])
            else:
                if seat_counter == number_of_occupied_seats:
                    seats_to_change_list.append([line_id, seat_id])

    return seats_to_change_list


def find_new_seating_state_part_2(ferry_data):
    new_state = deepcopy(ferry_data)

    # Finding seats to free up
    seats_to_replace = identify_visibly_occupied_seats(ferry_data, number_of_occupied_seats=5, goal='freeup')
    for record in seats_to_replace:
        new_state[record[0]][record[1]] = 'L'

    seats_to_replace = identify_visibly_occupied_seats(ferry_data, number_of_occupied_seats=0, goal='occupy')
    for record in seats_to_replace:
        new_state[record[0]][record[1]] = '#'

    return new_state


def find_final_occ_seats_count_part_2(ferry_data):
    previous_state = ferry_data
    current_state = None
    counter = 0

    while True:
        counter += 1
        current_state = find_new_seating_state_part_2(previous_state)

        if current_state == previous_state:
            break

        previous_state = current_state

    occupied_seats = sum(letter == '#' for line in current_state for letter in line)

    return occupied_seats


def run(ferry_info_file):
    with open(ferry_info_file, "r+") as file:
        ferry_data = [list(line.replace('\n', '')) for line in file.readlines()]

    part_1_result = find_final_occ_seats_count(ferry_data)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't count occupied seats.")

    part_2_result = find_final_occ_seats_count_part_2(ferry_data)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't count occupied seats.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
