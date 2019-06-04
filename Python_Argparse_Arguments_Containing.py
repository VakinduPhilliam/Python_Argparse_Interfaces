# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Arguments containing -
# The parse_args() method attempts to give errors whenever the user has clearly made a mistake, but some situations are inherently ambiguous.
# For example, the command-line argument -1 could either be an attempt to specify an option or an attempt to provide a positional argument.
# The parse_args() method is cautious here: positional arguments may only begin with - if they look like negative numbers and there are no options in the
# parser that look like negative numbers:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x')

parser.add_argument('foo', nargs='?')

# no negative number options, so -1 is a positional argument

parser.parse_args(['-x', '-1'])

# OUTPUT: 'Namespace(foo=None, x='-1')'

# no negative number options, so -1 and -5 are positional arguments

parser.parse_args(['-x', '-1', '-5'])

# OUTPUT: 'Namespace(foo='-5', x='-1')'

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-1', dest='one')

parser.add_argument('foo', nargs='?')

# negative number options present, so -1 is an option

parser.parse_args(['-1', 'X'])

# OUTPUT: 'Namespace(foo=None, one='X')'

# negative number options present, so -2 is an option

parser.parse_args(['-2'])

# negative number options present, so both -1s are options

parser.parse_args(['-1', '-1'])

#
# If you have positional arguments that must begin with - and don’t look like negative numbers, you can insert the pseudo-argument '--' which tells
# parse_args() that everything after that is a positional argument:
# 

parser.parse_args(['--', '-f'])

# OUTPUT: 'Namespace(foo='-f', one=None)'
