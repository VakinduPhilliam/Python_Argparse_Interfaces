# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
# 
# name or flags
# The add_argument() method must know whether an optional argument, like -f or --foo, or a positional argument, like a list of filenames, is expected.
# The first arguments passed to add_argument() must therefore be either a series of flags, or a simple argument name. For example, an optional argument
# could be created like:
# 

parser.add_argument('-f', '--foo')

# 
# while a positional argument could be created like:
# 

parser.add_argument('bar')
 
#
# When parse_args() is called, optional arguments will be identified by the - prefix, and the remaining arguments will be assumed to be positional:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo')

parser.add_argument('bar')

parser.parse_args(['BAR'])

# OUTPUT: 'Namespace(bar='BAR', foo=None)'

parser.parse_args(['BAR', '--foo', 'FOO'])

# OUTPUT: 'Namespace(bar='BAR', foo='FOO')'

parser.parse_args(['--foo', 'FOO'])
