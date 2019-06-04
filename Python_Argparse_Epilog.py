# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# epilog.
# Some programs like to display additional description of the program after the description of the arguments.
# Such text can be specified using the epilog= argument to ArgumentParser:
# 

parser = argparse.ArgumentParser(
        description='A foo that bars',
        epilog="And that's how you'd foo a bar")

parser.print_help()
