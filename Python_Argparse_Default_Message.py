# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# By default, ArgumentParser calculates the usage message from the arguments it contains:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', nargs='?', help='foo help')

parser.add_argument('bar', nargs='+', help='bar help')

parser.print_help()
 
#
# The default message can be overridden with the usage= keyword argument:
# 

parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('--foo', nargs='?', help='foo help')

parser.add_argument('bar', nargs='+', help='bar help')

parser.print_help()
