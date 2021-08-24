import sys


def get_filepath_from_command_line():
    _, *args = list(sys.argv)
    if len(args) != 1:
        raise ValueError('Expected only 1 argument, got {} instead'.format(args))
    filepath = args[0]
    return filepath
