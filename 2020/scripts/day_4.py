import re

from utils import get_filepath_from_command_line

def validate_passport_data(passport_data):
    validation_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passport_counter = 0

    for person_value in passport_data:
        number_of_valid_fields = len([
            sub_key
            for key in person_value.strip().split(' ')
            for sub_key in key.split(':')
            if (sub_key in validation_list)
        ])
        if number_of_valid_fields == len(validation_list):
            valid_passport_counter += 1

    return valid_passport_counter


def validate_all_passport_data(passport_data):
    valid_passport_counter = 0

    for person_value in passport_data:
        valid_field_counter = 0
        for field in person_value.strip().split(' '):
            field_key, field_value = field.split(':')

            if field_key.lower() == 'byr':
                if 1920 <= int(field_value) <= 2002:
                    valid_field_counter += 1

            if field_key.lower() == 'iyr':
                if int(field_value) >= 2010 and int(field_value) <= 2020:
                    valid_field_counter += 1

            if field_key.lower() == 'eyr':
                if int(field_value) >= 2020 and int(field_value) <= 2030:
                    valid_field_counter += 1

            if field_key.lower() == 'hgt':
                if 'cm' in field_value:
                    height_value = int(field_value.replace('cm', ''))
                    if height_value >= 150 and height_value <= 193:
                        valid_field_counter += 1
                if 'in' in field_value:
                    height_value = int(field_value.replace('in', ''))
                    if height_value >= 59 and height_value <= 76:
                        valid_field_counter += 1

            if field_key.lower() == 'ecl':
                eye_color_list = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
                if field_value in eye_color_list:
                    valid_field_counter += 1

            if field_key.lower() == 'hcl':
                if re.fullmatch('#[a-fA-F0-9]{6}', field_value) is not None:
                    valid_field_counter += 1

            if field_key.lower() == 'pid':
                if re.fullmatch('[0-9]{9}', field_value) is not None:
                    valid_field_counter += 1

        if valid_field_counter == 7:
            valid_passport_counter += 1

    return valid_passport_counter


def run(passport_data_file):
    with open(passport_data_file, "r+") as file:
        passport_data = [passport_line.replace('\n', ' ') for passport_line in file.read().split('\n\n')]

    part_1_result = validate_passport_data(passport_data)

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't validate passport data.")

    part_2_result = validate_all_passport_data(passport_data)

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't validate all passport data components.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)



