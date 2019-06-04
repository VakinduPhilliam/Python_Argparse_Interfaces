# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Beyond sys.argv
# Sometimes it may be useful to have an ArgumentParser parse arguments other than those of sys.argv.
# This can be accomplished by passing a list of strings to parse_args().
# This is useful for testing at the interactive prompt:
# 

parser = argparse.ArgumentParser()

parser.add_argument(
        'integers', metavar='int', type=int, choices=range(10),
        nargs='+', help='an integer in the range 0..9')

parser.add_argument(
        '--sum', dest='accumulate', action='store_const', const=sum,
        default=max, help='sum the integers (default: find the max)')

parser.parse_args(['1', '2', '3', '4'])

# OUTPUT: 'Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])'

parser.parse_args(['1', '2', '3', '4', '--sum'])
