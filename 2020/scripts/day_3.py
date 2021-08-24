import math
import numpy as np

from utils import get_filepath_from_command_line


def count_trees(map_info, long=1, lat=3):
    tree_count = 0

    while long <= (len(map_info[0]) - 1) and lat <= (len(map_info) - 1):
        if map_info[lat][long] == '#':
            tree_count += 1
        long += 3
        lat += 1

    return tree_count


def create_proper_sized_map(map_pattern, slope_steps_down, slope_steps_right):
    total_steps_down = len(map_pattern) / slope_steps_down
    map_multiplier = math.ceil(total_steps_down / len(map_pattern[0]))
    full_size_map = [map_string * map_multiplier * slope_steps_right for map_string in map_pattern]
    return full_size_map


def count_trees_multiple_scenarios(map_info, slope_scenarios=([1, 1], [1, 3], [1, 5], [1, 7], [2, 1])):
    trees_counter_list = []

    for slope_scenario in slope_scenarios:
        full_size_map = create_proper_sized_map(map_info, slope_scenario[0], slope_scenario[1])

        long = slope_scenario[1]
        lat = slope_scenario[0]
        tree_count = 0

        while long <= (len(full_size_map[0]) - 1) and lat <= (len(full_size_map) - 1):
            if full_size_map[lat][long] == '#':
                tree_count += 1
            long += slope_scenario[1]
            lat += slope_scenario[0]

        trees_counter_list.append(tree_count)

    return np.prod(trees_counter_list)


def run(map_info_file):
    with open(map_info_file, "r+") as file:
        map_info = [map_line.replace('\n', '') for map_line in file.readlines()]

    map_info_wide = [map_string * 33 for map_string in map_info]

    part_1_result = count_trees(map_info_wide)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't count trees encountered on the specified route.")

    part_2_result = count_trees_multiple_scenarios(map_info)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't find product of tree count in all specified slope scenarios.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
