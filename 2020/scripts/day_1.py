from utils import get_filepath_from_command_line


def find_product_of_two_entries_sum_up_to_value(expense_int_list, sum_up_value=2020):
    expense_int_list = sorted(expense_int_list)

    result_list = set()

    for expense_i in expense_int_list:
        if expense_i not in result_list:
            for expense_j in expense_int_list:
                if expense_i + expense_j == sum_up_value:
                    result_list.add(expense_j)
                    return expense_i * expense_j


def find_product_of_three_entries_sum_up_to_value(expense_int_list, sum_up_value=2020):
    expense_int_list = sorted(expense_int_list)

    for expense_i in expense_int_list:
        for expense_j in expense_int_list:
            for expense_k in expense_int_list:
                if expense_i + expense_j + expense_k == sum_up_value:
                    return expense_i * expense_j * expense_k


def run(expense_report_file):
    with open(expense_report_file, "r+") as file:
        expense_int_list = [int(line) for line in file.read().split()]

    part_1_result = find_product_of_two_entries_sum_up_to_value(expense_int_list)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't find product of two entries.")

    part_2_result = find_product_of_three_entries_sum_up_to_value(
        expense_int_list
    )

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't find product of three entries.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
