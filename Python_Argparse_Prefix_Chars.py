# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# prefix_chars
# Most command-line options will use - as the prefix, e.g. -f/--foo. Parsers that need to support different or additional prefix characters,
# e.g. for options like +f or /foo, may specify them using the prefix_chars= argument to the ArgumentParser constructor:
# 

parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
parser.add_argument('+f')

parser.add_argument('++bar')

parser.parse_args('+f X ++bar Y'.split())
