# Python argparse
# argparse � Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# default
# All optional arguments and some positional arguments may be omitted at the command line. The default keyword argument of add_argument(), whose value
# defaults to None, specifies what value should be used if the command-line argument is not present.
#
# For optional arguments, the default value is used when the option string was not present at the command line:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=42)

parser.parse_args(['--foo', '2'])

# OUTPUT: 'Namespace(foo='2')'

parser.parse_args([])

# OUTPUT: 'Namespace(foo=42)'
 
#
# If the default value is a string, the parser parses the value as if it were a command-line argument.
# In particular, the parser applies any type conversion argument, if provided, before setting the attribute on the Namespace return value.
# Otherwise, the parser uses the value as is:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--length', default='10', type=int)

parser.add_argument('--width', default=10.5, type=int)

parser.parse_args()

# OUTPUT: 'Namespace(length=10, width=10.5)'
 
#
# For positional arguments with nargs equal to ? or *, the default value is used when no command-line argument was present:
# 

parser = argparse.ArgumentParser()
parser.add_argument('foo', nargs='?', default=42)

parser.parse_args(['a'])

# OUTPUT: 'Namespace(foo='a')'

parser.parse_args([])

# OUTPUT: 'Namespace(foo=42)'
 
#
# Providing default=argparse.SUPPRESS causes no attribute to be added if the command-line argument was not present:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', default=argparse.SUPPRESS)

parser.parse_args([])

# OUTPUT: 'Namespace()'

parser.parse_args(['--foo', '1'])

# OUTPUT: 'Namespace(foo='1')'
