# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
# Parsing arguments.
# ArgumentParser parses arguments through the parse_args() method. This will inspect the command line, convert each argument to the appropriate type and
# then invoke the appropriate action. In most cases, this means a simple Namespace object will be built up from attributes parsed out of the command line:
 
parser.parse_args(['--sum', '7', '-1', '42'])

# OUTPUT: 'Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])'

# 
# In a script, parse_args() will typically be called with no arguments, and the ArgumentParser will automatically determine the command-line arguments from
# sys.argv.
#