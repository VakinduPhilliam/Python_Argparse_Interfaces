# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
# 
# argument_default
#
# Generally, argument defaults are specified either by passing a default to add_argument() or by calling the set_defaults() methods with a specific set of
# name-value pairs. Sometimes however, it may be useful to specify a single parser-wide default for arguments. This can be accomplished by passing the
# argument_default= keyword argument to ArgumentParser. For example, to globally suppress attribute creation on parse_args() calls, we supply
# argument_default=SUPPRESS:
# 

parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('--foo')

parser.add_argument('bar', nargs='?')

parser.parse_args(['--foo', '1', 'BAR'])

# OUTPUT: 'Namespace(bar='BAR', foo='1')'

parser.parse_args([])

# OUTPUT: 'Namespace()'
