# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
#
# Mutual exclusion.
# ArgumentParser.add_mutually_exclusive_group(required=False). 
# Create a mutually exclusive group. argparse will make sure that only one of the arguments in the mutually exclusive group was present on the command line:
 
parser = argparse.ArgumentParser(prog='PROG')

group = parser.add_mutually_exclusive_group()
group.add_argument('--foo', action='store_true')

group.add_argument('--bar', action='store_false')

parser.parse_args(['--foo'])

# OUTPUT 'Namespace(bar=True, foo=True)'

parser.parse_args(['--bar'])

# OUTPUT 'Namespace(bar=False, foo=False)'

parser.parse_args(['--foo', '--bar'])

# 
# The add_mutually_exclusive_group() method also accepts a required argument, to indicate that at least one of the mutually exclusive arguments is required:
# 

parser = argparse.ArgumentParser(prog='PROG')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--foo', action='store_true')

group.add_argument('--bar', action='store_false')

parser.parse_args([])

#
# Note that currently mutually exclusive argument groups do not support the title and description arguments of add_argument_group().
#