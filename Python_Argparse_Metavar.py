# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# metavar:
# When ArgumentParser generates help messages, it needs some way to refer to each expected argument. By default, ArgumentParser objects use the dest value
# as the “name” of each object. By default, for positional argument actions, the dest value is used directly, and for optional argument actions, the dest
# value is uppercased. So, a single positional argument with dest='bar' will be referred to as bar. A single optional argument --foo that should be followed
# by a single command-line argument will be referred to as FOO.
#
# An example:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo')

parser.add_argument('bar')

parser.parse_args('X --foo Y'.split())

# OUTPUT: 'Namespace(bar='X', foo='Y')'

parser.print_help()

#
# An alternative name can be specified with metavar:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', metavar='YYY')

parser.add_argument('bar', metavar='XXX')

parser.parse_args('X --foo Y'.split())

# OUTPUT: 'Namespace(bar='X', foo='Y')'

parser.print_help()

# 
# Note that metavar only changes the displayed name - the name of the attribute on the parse_args() object is still determined by the dest value.
# Different values of nargs may cause the metavar to be used multiple times. Providing a tuple to metavar specifies a different display for each of the
# arguments:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x', nargs=2)

parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))

parser.print_help()
