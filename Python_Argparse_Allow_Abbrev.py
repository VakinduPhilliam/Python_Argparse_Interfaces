# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# allow_abbrev
# Normally, when you pass an argument list to the parse_args() method of an ArgumentParser, it recognizes abbreviations of long options.
# This feature can be disabled by setting allow_abbrev to False:
 
parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
parser.add_argument('--foobar', action='store_true')

parser.add_argument('--foonley', action='store_false')

parser.parse_args(['--foon'])
