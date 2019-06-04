# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# MetavarTypeHelpFormatter uses the name of the type argument for each argument as the display name for its values (rather than using the dest as the
# regular formatter does):
 
parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.MetavarTypeHelpFormatter)

parser.add_argument('--foo', type=int)
parser.add_argument('bar', type=float)

parser.print_help()
