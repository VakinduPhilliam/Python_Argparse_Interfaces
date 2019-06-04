# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Intermixed parsing.
# ArgumentParser.parse_intermixed_args(args=None, namespace=None) ArgumentParser.parse_known_intermixed_args(args=None, namespace=None).
# A number of Unix commands allow the user to intermix optional arguments with positional arguments. The parse_intermixed_args() and
# parse_known_intermixed_args() methods support this parsing style.
# 
# These parsers do not support all the argparse features, and will raise exceptions if unsupported features are used. In particular, subparsers, 
# argparse.REMAINDER, and mutually exclusive groups that include both optionals and positionals are not supported.
# 
# The following example shows the difference between parse_known_args() and parse_intermixed_args(): the former returns ['2', '3'] as unparsed arguments,
# while the latter collects all the positionals into rest.
# 

parser = argparse.ArgumentParser()

parser.add_argument('--foo')
parser.add_argument('cmd')

parser.add_argument('rest', nargs='*', type=int)

parser.parse_known_args('doit 1 --foo bar 2 3'.split())

parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
