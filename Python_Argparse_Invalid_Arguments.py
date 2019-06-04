# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Invalid arguments.
# While parsing the command line, parse_args() checks for a variety of errors, including ambiguous options, invalid types, invalid options, wrong number of
# positional arguments, etc.
# When it encounters such an error, it exits and prints the error along with a usage message:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', type=int)

parser.add_argument('bar', nargs='?')

# invalid type

parser.parse_args(['--foo', 'spam'])

# invalid option

parser.parse_args(['--bar'])

# wrong number of arguments

parser.parse_args(['spam', 'badger'])
