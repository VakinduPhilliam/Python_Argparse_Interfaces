# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
#
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Passing RawDescriptionHelpFormatter as formatter_class= indicates that description and epilog are already correctly formatted and should not be
# line-wrapped:
 
parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Please do not mess up this text!
            --------------------------------
                I have indented it
                exactly the way
                I want it
            '''))

parser.print_help()
