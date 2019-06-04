# Python Argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Creating a parser.
# The first step in using the argparse is creating an ArgumentParser object:
#
# The ArgumentParser object will hold all the information necessary to parse the command line into Python data types.
#

parser = argparse.ArgumentParser(description='Process some integers.')
