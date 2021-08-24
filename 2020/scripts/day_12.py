import re

from itertools import islice, cycle
from utils import get_filepath_from_command_line

# Part 1
def move_ship_in_certain_direction(number_of_units, move_direction, initial_long, initial_lat, curr_direction):
    direction_multiplier = {'E': 1, 'W': -1, 'N': 1, 'S': -1}

    if move_direction not in ['E', 'W', 'S', 'N']:
        raise ValueError('Verify the direction. It should be one of these: E, W, S, N.')

    if move_direction in ['E', 'W']:
        new_long = initial_long + number_of_units * direction_multiplier[move_direction]
        new_lat = initial_lat

    elif move_direction in ['N', 'S']:
        new_long = initial_long
        new_lat = initial_lat + number_of_units * direction_multiplier[move_direction]

    return [new_long, new_lat, curr_direction]


def rotate_ship_in_certain_direction(degrees, direction, initial_long, initial_lat, current_direction):
    if direction not in ['L', 'R']:
        raise ValueError('Verify the direction. The value should be L or R')

    if direction == 'R':
        direction_list = ['E', 'S', 'W', 'N']
    else:
        direction_list = ['E', 'N', 'W', 'S']

    number_of_changes = int(degrees / 90)
    direction_index = direction_list.index(current_direction)

    new_direction = list(islice(cycle(direction_list),
                                direction_index + 1,
                                direction_index + 1 + number_of_changes))[-1]

    return [initial_long, initial_lat, new_direction]


def follow_ship_direction_instructions(direction_data):
    long = 0
    lat = 0
    ship_direction = 'E'

    for direction_line in direction_data:
        direction = direction_line[0]
        change_value = direction_line[1]
        # print(direction, change_value)

        if direction in {'E', 'S', 'W', 'N'}:
            long, lat, ship_direction = move_ship_in_certain_direction(change_value, direction, long, lat,
                                                                       ship_direction)

        elif direction in {'R', 'L'}:
            long, lat, ship_direction = rotate_ship_in_certain_direction(change_value, direction, long, lat,
                                                                         ship_direction)

        elif direction == 'F':
            long, lat, ship_direction = move_ship_in_certain_direction(change_value, ship_direction, long, lat,
                                                                       ship_direction)
        else:
            raise ValueError('Direction value is incorrect.')

    return sum([abs(long), abs(lat)])


# Part 2
def move_waypoint(curr_waypoint_long, curr_waypoint_long_dir,
                  current_waypoint_lat, curr_waypoint_lat_dir, change_direction, number_of_change_units):
    if change_direction not in ['E', 'W', 'S', 'N']:
        raise ValueError('Verify the direction. It should be one of these: E, W, S, N.')

    if change_direction in ['E', 'W']:
        if change_direction == curr_waypoint_long_dir:
            direction_multiplier = 1
        else:
            direction_multiplier = -1

        new_waypoint_long = curr_waypoint_long + number_of_change_units * direction_multiplier
        new_waypoint_lat = current_waypoint_lat

    elif change_direction in ['N', 'S']:
        if change_direction == curr_waypoint_lat_dir:
            direction_multiplier = 1
        else:
            direction_multiplier = -1

        new_waypoint_long = curr_waypoint_long
        new_waypoint_lat = current_waypoint_lat + number_of_change_units * direction_multiplier

    return new_waypoint_long, curr_waypoint_long_dir, new_waypoint_lat, curr_waypoint_lat_dir


def rotate_waypoint(curr_waypoint_long, curr_waypoint_long_dir,
                    curr_waypoint_lat, curr_waypoint_lat_dir, rotation_dir, degrees):
    if rotation_dir not in ('L', 'R'):
        raise ValueError('Check rotation direction. Can only be L or R')

    if rotation_dir == 'R':
        direction_list = [['E', 'N'], ['E', 'S'], ['W', 'S'], ['W', 'N']]
    else:
        direction_list = [['E', 'N'], ['W', 'N'], ['W', 'S'], ['E', 'S']]

    number_of_changes = int(degrees / 90)
    direction_index = direction_list.index([curr_waypoint_long_dir, curr_waypoint_lat_dir])
    # print(number_of_changes, direction_index)

    new_directions = list(islice(cycle(direction_list),
                                 direction_index + 1,
                                 direction_index + 1 + number_of_changes))[-1]

    values_list = [curr_waypoint_long, curr_waypoint_lat]

    for i in range(number_of_changes):
        values_list = values_list[::-1]

    curr_waypoint_long, curr_waypoint_lat = values_list

    return curr_waypoint_long, new_directions[0], curr_waypoint_lat, new_directions[1]


def move_ship_towards_waypoint(curr_long, curr_lat,
                               waypoint_long, waypoint_long_dir, waypoint_lat, waypoint_lat_dir, change_value):
    dir_mult_dict = {'N': 1, 'E': 1, 'S': -1, 'W': -1}
    long_dir_mult = dir_mult_dict[waypoint_long_dir]
    lat_dir_mult = dir_mult_dict[waypoint_lat_dir]

    long = curr_long + change_value * waypoint_long * long_dir_mult
    lat = curr_lat + change_value * waypoint_lat * lat_dir_mult

    return long, lat


def follow_ship_direction_instructions_part2(direction_data):
    ship_long = 0
    ship_lat = 0
    waypoint_long_dir = 'E'
    waypoint_long = 10
    waypoint_lat_dir = 'N'
    waypoint_lat = 1

    for direction_line in direction_data:
        direction = direction_line[0]
        change_value = direction_line[1]

        if direction in {'E', 'S', 'W', 'N'}:
            waypoint_long, waypoint_long_dir, waypoint_lat, waypoint_lat_dir = move_waypoint(waypoint_long,
                                                                                             waypoint_long_dir,
                                                                                             waypoint_lat,
                                                                                             waypoint_lat_dir,
                                                                                             direction,
                                                                                             change_value)

        elif direction in {'L', 'R'}:
            waypoint_long, waypoint_long_dir, waypoint_lat, waypoint_lat_dir = rotate_waypoint(waypoint_long,
                                                                                               waypoint_long_dir,
                                                                                               waypoint_lat,
                                                                                               waypoint_lat_dir,
                                                                                               direction,
                                                                                               change_value)

        elif direction == 'F':
            ship_long, ship_lat = move_ship_towards_waypoint(ship_long, ship_lat, waypoint_long,
                                                             waypoint_long_dir,
                                                             waypoint_lat,
                                                             waypoint_lat_dir,
                                                             change_value)

        else:
            raise ValueError('Direction value is incorrect.')

    return sum([abs(ship_long), abs(ship_lat)])


def run(ship_directions_file):
    with open(ship_directions_file, "r+") as file:
        ship_directions_data = file.read().split()

    direction_pattern = r'([a-zA-Z]{1})([0-9]*)'
    direction_step_parsed = [[re.search(direction_pattern, direction_step).group(1),
                              int(re.search(direction_pattern, direction_step).group(2))]
                             for direction_step in ship_directions_data]

    part_1_result = follow_ship_direction_instructions(direction_step_parsed)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't calculate ship's Manhattan distance for part 1.")

    part_2_result = follow_ship_direction_instructions_part2(direction_step_parsed)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't calculate ship's Manhattan distance for part 2.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)