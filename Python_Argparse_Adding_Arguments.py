# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Adding arguments.
# Filling an ArgumentParser with information about program arguments is done by making calls to the add_argument() method. Generally, these calls tell the
# ArgumentParser how to take the strings on the command line and turn them into objects. This information is stored and used when parse_args() is called.
#
# For example:
# 

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
 
#
# Later, calling parse_args() will return an object with two attributes, integers and accumulate.
# The integers attribute will be a list of one or more ints, and the accumulate attribute will be either the sum() function, if --sum was specified at the
# command line, or the max() function if it was not.
#