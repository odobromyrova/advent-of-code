from collections import defaultdict
from copy import copy
from utils import get_filepath_from_command_line


def preprocess_adapter_data(adapter_info_clean):
    adapter_info_new = copy(adapter_info_clean)
    adapter_info_new = sorted(adapter_info_new)
    device_adapter = max(adapter_info_clean) + 3
    adapter_info_new.append(device_adapter)
    return adapter_info_new


def find_adapter_diff_dist(adapter_info_clean, built_in_adapter_diff=3):
    adapter_info_new = preprocess_adapter_data(adapter_info_clean)
    count_one_diff = 0
    count_three_diff = 0
    prev_value = 0

    for ind, adapter in enumerate(adapter_info_new):
        adapter_jolt_diff = adapter - prev_value
        if adapter_jolt_diff <= 3:
            prev_value = adapter
            if adapter_jolt_diff == 1:
                count_one_diff += 1
            else:
                count_three_diff += 1
        else:
            print('Adapter chain can\'t be completed')

    return count_one_diff * count_three_diff


def count_unique_adapter_arrangements(adapter_info_clean):
    adapter_info_new = preprocess_adapter_data(adapter_info_clean)

    counts = defaultdict(int, {0: 1})

    # inspired by viliampucik solution
    for a_i in adapter_info_new:
        # number of ways to reach i-th adapter from the previous three
        counts[a_i] = counts[a_i - 3] + counts[a_i - 2] + counts[a_i - 1]

    return counts[adapter_info_new[-1]]


def run(adapter_info_file):
    with open(adapter_info_file, "r+") as file:
        adapter_info_clean = [int(line.replace('\n', '')) for line in file.readlines()]

    part_1_result = find_adapter_diff_dist(adapter_info_clean)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't calculate jolt differences.")

    part_2_result = count_unique_adapter_arrangements(adapter_info_clean)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't calculate number of distinct adapter arrangements.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
