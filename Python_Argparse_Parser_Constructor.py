# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
#
# Most calls to the ArgumentParser constructor will use the description= keyword argument. This argument gives a brief description of what the program does
# and how it works. In help messages, the description is displayed between the command-line usage string and the help messages for the various arguments:
 
parser = argparse.ArgumentParser(description='A foo that bars')

parser.print_help()
