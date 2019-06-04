# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
# 
# add_help
# 
# By default, ArgumentParser objects add an option which simply displays the parser’s help message. For example, consider a file named myprogram.py
# containing the following code:
# 

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')

args = parser.parse_args()
 
#
# If -h or --help is supplied at the command line, the ArgumentParser help will be printed:
# Occasionally, it may be useful to disable the addition of this help option. This can be achieved by passing False as the add_help= argument to
# ArgumentParser:
# 

parser = argparse.ArgumentParser(prog='PROG', add_help=False)
parser.add_argument('--foo', help='foo help')

parser.print_help()

# 
# The help option is typically -h/--help. The exception to this is if the prefix_chars= is specified and does not include -, in which case -h and --help
# are not valid options. In this case, the first character in prefix_chars is used to prefix the help options:
# 

parser = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
parser.print_help()
