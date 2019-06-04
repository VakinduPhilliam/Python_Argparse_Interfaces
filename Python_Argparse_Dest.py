# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# dest:
# Most ArgumentParser actions add some value as an attribute of the object returned by parse_args(). The name of this attribute is determined by the dest
# keyword argument of add_argument(). For positional argument actions, dest is normally supplied as the first argument to add_argument():
# 

parser = argparse.ArgumentParser()
parser.add_argument('bar')

parser.parse_args(['XXX'])

# OUTPUT: 'Namespace(bar='XXX')'

# 
# For optional argument actions, the value of dest is normally inferred from the option strings.
# ArgumentParser generates the value of dest by taking the first long option string and stripping away the initial -- string.
# If no long option strings were supplied, dest will be derived from the first short option string by stripping the initial - character.
# Any internal - characters will be converted to _ characters to make sure the string is a valid attribute name.
#
# The examples below illustrate this behavior:
# 

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--foo-bar', '--foo')

parser.add_argument('-x', '-y')

parser.parse_args('-f 1 -x 2'.split())

# OUTPUT: 'Namespace(foo_bar='1', x='2')'

parser.parse_args('--foo 1 -y 2'.split())

# OUTPUT: 'Namespace(foo_bar='1', x='2')'
 
#
# dest allows a custom attribute name to be provided:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', dest='bar')

parser.parse_args('--foo XXX'.split())

# OUTPUT: 'Namespace(bar='XXX')'
