from utils import get_filepath_from_command_line


def find_number_outlier(numbers_data_clean, preamble_length=25):
    iteration_range = range(preamble_length, len(numbers_data_clean))
    for i in iteration_range:
        list_to_check = numbers_data_clean[i - preamble_length: i]
        num_to_check = numbers_data_clean[i]
        match_counter = 0

        for num in list_to_check:
            for num2 in list_to_check:
                if num2 == num:
                    continue
                else:
                    if num + num2 == num_to_check:
                        match_counter += 1

        if match_counter == 0:
            return num_to_check


def find_contiguous_range(numbers_data_clean, outlier_number):
    original_range_end = len(numbers_data_clean)
    for num_ind in range(original_range_end):
        for range_ext in range(original_range_end - num_ind):
            new_range = numbers_data_clean[num_ind:num_ind+range_ext]
            if sum(new_range) == outlier_number:
                return min(new_range) + max(new_range)


def run(numbers_file):
    with open(numbers_file, "r+") as file:
        numbers_data_clean = [int(line.replace('\n', '')) for line in file.readlines()]

    part_1_result = find_number_outlier(numbers_data_clean)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't find outlying number.")

    part_2_result = find_contiguous_range(numbers_data_clean, part_1_result)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't find a contiguous set of numbers summing up to the outlier.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
