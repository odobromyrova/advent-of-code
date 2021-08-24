from copy import deepcopy
from utils import get_filepath_from_command_line


def find_acc_value_before_inf_loop(program_data_clean):
    steps_history = [0]
    acc_sum = 0

    for line_ind in steps_history:
        command_type, command_value = program_data_clean[line_ind]
        command_value = int(command_value)

        if command_type == 'acc':
            acc_sum += command_value
            next_step = line_ind + 1

        if command_type == 'nop':
            next_step = line_ind + 1

        if command_type == 'jmp':
            next_step = line_ind + command_value

        if next_step in steps_history:
            break

        else:
            steps_history.append(next_step)

    return acc_sum


def check_if_instructions_have_loop(program_data_clean):
    steps_history = [0]
    acc_sum = 0

    for line_ind in steps_history:
        command_type, command_value = program_data_clean[line_ind]
        command_value = int(command_value)

        if command_type == 'acc':
            acc_sum += command_value
            next_step = line_ind + 1

        if command_type == 'nop':
            next_step = line_ind + 1

        if command_type == 'jmp':
            next_step = line_ind + command_value

        if next_step in steps_history:
            return True, acc_sum

        elif next_step >= len(program_data_clean):
            return False, acc_sum
        else:
            steps_history.append(next_step)


def fix_instructions(program_data_clean):
    lines_to_check_ind = [index for index, line in enumerate(program_data_clean) if line[0] in ('nop', 'jmp')]
    for i in lines_to_check_ind:
        program_data_new = deepcopy(program_data_clean)
        record_to_update = program_data_new[i]
        if record_to_update[0] == 'jmp':
            record_to_update[0] = 'nop'
        elif record_to_update[0] == 'nop':
            record_to_update[0] = 'jmp'

        result_check, acc_sum = check_if_instructions_have_loop(program_data_new)

        if not result_check:
            return acc_sum


def run(program_data_file):
    with open(program_data_file, "r+") as file:
        program_data_clean = [line.replace('\n', '').split(' ') for line in file.readlines()]

    part_1_result = find_acc_value_before_inf_loop(program_data_clean)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't calculate the value in the accumulator before the loop.")

    part_2_result = fix_instructions(program_data_clean)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't calculate the value in the accumulator after the program terminates.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
