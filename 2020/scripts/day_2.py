from utils import get_filepath_from_command_line


def process_password_info_string(password_info_string):
    letter_occurrence, letter, password = password_info_string.replace(":", "").split(
        " "
    )
    letter_occurrence_min, letter_occurrence_max = letter_occurrence.split("-")
    return int(letter_occurrence_min), int(letter_occurrence_max), letter, password


def validate_password(password_info_list):
    valid_password_counter = 0

    for password_info_string in password_info_list:
        (
            letter_occurrence_min,
            letter_occurrence_max,
            letter,
            password,
        ) = process_password_info_string(password_info_string)
        letter_counter = password.count(letter)

        if letter_occurrence_min <= letter_counter <= letter_occurrence_max:
            valid_password_counter += 1

    return valid_password_counter


def validate_password_letter_position(password_info_list):
    valid_password_counter = 0

    for password_info_string in password_info_list:
        (
            letter_position_first,
            letter_position_second,
            letter,
            password,
        ) = process_password_info_string(password_info_string)

        letter_at_position_one = password[letter_position_first - 1]
        letter_at_position_two = password[letter_position_second - 1]

        if (
            letter_at_position_one == letter or letter_at_position_two == letter
        ) and letter_at_position_one != letter_at_position_two:
            valid_password_counter += 1

    return valid_password_counter


def run(password_info_file):
    with open(password_info_file, "r+") as file:
        password_list = file.read().strip().split("\n")

    part_1_result = validate_password(password_list)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't validate the password.")

    part_2_result = validate_password_letter_position(password_list)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't validate the password.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
