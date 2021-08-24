import re

from utils import get_filepath_from_command_line


def identify_bag_containing_certain_color_directly(bags_info_clean, color_name):
    list_of_bags_containing_color_directly = []

    content_color_flag = r'contain .* ({} bag)'.format(color_name)
    container_bag_pattern = r'.+?(?= bags contain)'

    for bag_info in bags_info_clean:
        bag_content_match = re.search(content_color_flag, bag_info)
        if bag_content_match is not None:
            if bag_content_match.group(1) == '{} bag'.format(color_name):
                container_bag = re.search(container_bag_pattern, bag_info).group()
                list_of_bags_containing_color_directly.append(container_bag)

    return list_of_bags_containing_color_directly


def find_all_bags_that_can_contain_color(bags_info_clean, color):
    container_colors_list = identify_bag_containing_certain_color_directly(bags_info_clean, color)
    for container_color in container_colors_list:
        new_container_colors_list = identify_bag_containing_certain_color_directly(bags_info_clean, container_color)
        container_colors_list += new_container_colors_list

    return len(set(container_colors_list))


def encode_content_rules(bags_info_clean):
    structure_dict = {}

    for bag_info_line in bags_info_clean:
        main_bag_regex = r'.+?(?= bags contain)'
        main_bag = re.search(main_bag_regex, bag_info_line).group()

        bags_inside_regex = r'([0-9])+ ([a-z]* [a-z]*)'
        bags_inside_result = re.findall(bags_inside_regex, bag_info_line)

        if bags_inside_result == []:
            structure_dict[main_bag] = []

        else:
            list_of_bags = []
            for bag_inside in bags_inside_result:
                list_of_bags.append({'color': bag_inside[1], 'count': bag_inside[0]})

            structure_dict[main_bag] = list_of_bags
            # structure_dict[main_bag] = [{'color': 'lavender', 'count': 5}, {'color': 'shiny maroon', 'count': 6}]

    return structure_dict


def count_awesome_bags_recursively(tree_structure_dict, color):
    components = tree_structure_dict[color]

    if len(components) == 0:
        return 0

    total_bags = 0

    for component in components:
        component_color = component['color']
        component_count = int(component['count'])
        total_bags += component_count + component_count * count_awesome_bags_recursively(tree_structure_dict,
                                                                                         component_color)
    return total_bags


def run(bags_info_file):
    with open(bags_info_file, "r+") as file:
        bags_info = [line.replace('\n', '') for line in file.readlines()]

    bags_info_tree = encode_content_rules(bags_info)

    part_1_result = find_all_bags_that_can_contain_color(bags_info, 'shiny gold')

    if part_1_result is not None:
        print("Part 1 result: ", part_1_result)
    else:
        print("Couldn't calculate number of colors of bags within one shiny gold bag.")

    part_2_result = count_awesome_bags_recursively(bags_info_tree, 'shiny gold')

    if part_2_result is not None:
        print("Part 2 result: ", part_2_result)

    else:
        print("Couldn't calculate number of individual bags within one shiny gold bag.")


if __name__ == "__main__":
    filepath = get_filepath_from_command_line()
    run(filepath)
