# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Argument abbreviations (prefix matching):
# The parse_args() method by default allows long options to be abbreviated to a prefix, if the abbreviation is unambiguous (the prefix matches a unique
# option):
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-bacon')

parser.add_argument('-badger')

parser.parse_args('-bac MMM'.split())

# OUTPUT: 'Namespace(bacon='MMM', badger=None)'

parser.parse_args('-bad WOOD'.split())

# OUTPUT: 'Namespace(bacon=None, badger='WOOD')'

parser.parse_args('-ba BA'.split())
