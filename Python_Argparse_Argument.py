# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
#
# RawTextHelpFormatter maintains whitespace for all sorts of help text, including argument descriptions. However, multiple new lines are replaced with one.
# If you wish to preserve multiple blank lines, add spaces between the newlines.
# 
# ArgumentDefaultsHelpFormatter automatically adds information about default values to each of the argument help messages:
# 

parser = argparse.ArgumentParser(
        prog='PROG',
       formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--foo', type=int, default=42, help='FOO!')
parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')

parser.print_help()
