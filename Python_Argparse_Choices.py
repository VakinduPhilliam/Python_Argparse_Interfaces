# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# choices
# Some command-line arguments should be selected from a restricted set of values. These can be handled by passing a container object as the choices keyword
# argument to add_argument(). When the command line is parsed, argument values will be checked, and an error message will be displayed if the argument was
# not one of the acceptable values:
# 

parser = argparse.ArgumentParser(prog='game.py')
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])

parser.parse_args(['rock'])

# OUTPUT: 'Namespace(move='rock')'

parser.parse_args(['fire'])

#
# Note that inclusion in the choices container is checked after any type conversions have been performed, so the type of the objects in the choices
# container should match the type specified:
# 

parser = argparse.ArgumentParser(prog='doors.py')
parser.add_argument('door', type=int, choices=range(1, 4))

print(parser.parse_args(['3']))

# OUTPUT: 'Namespace(door=3)'

parser.parse_args(['4'])

#
# Any object that supports the in operator can be passed as the choices value, so dict objects, set objects, custom containers, etc. are all supported.
#