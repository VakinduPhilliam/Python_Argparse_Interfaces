# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# The parse_args() method
# ArgumentParser.parse_args(args=None, namespace=None) 
# Convert argument strings to objects and assign them as attributes of the namespace. Return the populated namespace.
#
# Option value syntax:
# The parse_args() method supports several ways of specifying the value of an option (if it takes one).
# In the simplest case, the option and its value are passed as two separate arguments:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x')

parser.add_argument('--foo')

parser.parse_args(['-x', 'X'])

# OUTPUT: 'Namespace(foo=None, x='X')'

parser.parse_args(['--foo', 'FOO'])

# OUTPUT: 'Namespace(foo='FOO', x=None)'
 
#
# For long options (options with names longer than a single character), the option and value can also be passed as a single command-line argument,
# using = to separate them:
# 

parser.parse_args(['--foo=FOO'])

# OUTPUT: 'Namespace(foo='FOO', x=None)'
 
#
# For short options (options only one character long), the option and its value can be concatenated:
# 

parser.parse_args(['-xX'])

# OUTPUT: 'Namespace(foo=None, x='X')'

# 
# Several short options can be joined together, using only a single - prefix, as long as only the last option (or none of them) requires a value:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x', action='store_true')

parser.add_argument('-y', action='store_true')

parser.add_argument('-z')

parser.parse_args(['-xyzZ'])

# OUTPUT: 'Namespace(x=True, y=True, z='Z')'
