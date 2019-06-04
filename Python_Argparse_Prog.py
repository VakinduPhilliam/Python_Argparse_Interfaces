# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
# prog.
# By default, ArgumentParser objects use sys.argv[0] to determine how to display the name of the program in help messages.
# This default is almost always desirable because it will make the help messages match how the program was invoked on the command line.
#
# For example, consider a file named myprogram.py with the following code:
# 

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')

args = parser.parse_args()
