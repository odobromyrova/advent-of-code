from utils import get_filepath_from_command_line


def count_yes_answers(grouped_answers):
    count = 0

    for group_answers in grouped_answers:
        count += len(set(''.join(group_answers)))

    return count


def calculate_yes_per_question_in_group(group_answers_list):
    unanimous_yes_cnt = 0

    n_group_members = len(group_answers_list)
    linked_group_string = ''.join(group_answers_list)
    unique_answers = set(linked_group_string)

    for unique_answer in unique_answers:
        number_of_yes_per_question = sum(letter == unique_answer for letter in linked_group_string)
        if number_of_yes_per_question == n_group_members:
            unanimous_yes_cnt += 1

    return unanimous_yes_cnt


def count_unanimous_yes_answers(grouped_answers):
    total_unanimous_answers_cnt = 0

    for group_answers in grouped_answers:
        yes_cnt_per_group = calculate_yes_per_question_in_group(group_answers)
        total_unanimous_answers_cnt += yes_cnt_per_group

    return total_unanimous_answers_cnt


def run(grouped_answers_file):
    with open(grouped_answers_file, "r+") as file:
        grouped_answers = [line.strip().split('\n') for line in file.read().split('\n\n')]

    part_1_result = count_yes_answers(grouped_answers)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't count yes answers.")

    part_2_result = count_unanimous_yes_answers(grouped_answers)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't calculate unanimous yes answers.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)

