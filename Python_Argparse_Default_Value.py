# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# To change this default behavior, another value can be supplied using the prog= argument to ArgumentParser:
# 

parser = argparse.ArgumentParser(prog='myprogram')

parser.print_help()
