# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# action
# ArgumentParser objects associate command-line arguments with actions. These actions can do just about anything with the command-line arguments associated
# with them, though most actions simply add an attribute to the object returned by parse_args().
# The action keyword argument specifies how the command-line arguments should be handled.
#
# The supplied actions are:
#
# > 'store' - This just stores the argument’s value. This is the default action.
#
# For example:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo')

parser.parse_args('--foo 1'.split())

# OUTPUT: 'Namespace(foo='1')'
 
# > 'store_const' - This stores the value specified by the const keyword argument. The 'store_const' action is most commonly used with optional arguments
# that specify some sort of flag.
#
# For example:
 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_const', const=42)

parser.parse_args(['--foo'])

# OUTPUT: 'Namespace(foo=42)'
 
# > 'store_true' and 'store_false' - These are special cases of 'store_const' used for storing the values True and False respectively.
# In addition, they create default values of False and True respectively.
#
# For example:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')

parser.add_argument('--bar', action='store_false')
parser.add_argument('--baz', action='store_false')

parser.parse_args('--foo --bar'.split())

# OUTPUT: 'Namespace(foo=True, bar=False, baz=True)'
 
# > 'append' - This stores a list, and appends each argument value to the list. This is useful to allow an option to be specified multiple times.
#
# Example usage:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='append')

parser.parse_args('--foo 1 --foo 2'.split())

# OUTPUT: 'Namespace(foo=['1', '2'])'
 
# > 'append_const' - This stores a list, and appends the value specified by the const keyword argument to the list.
# (Note that the const keyword argument defaults to None.) The 'append_const' action is typically useful when multiple arguments need to store constants to
# the same list.
#
# For example:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--str', dest='types', action='append_const', const=str)

parser.add_argument('--int', dest='types', action='append_const', const=int)

parser.parse_args('--str --int'.split())

# OUTPUT: 'Namespace(types=[<class 'str'>, <class 'int'>])'
 
# > 'count' - This counts the number of times a keyword argument occurs.
#
# For example, this is useful for increasing verbosity levels:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count')

parser.parse_args(['-vvv'])

# OUTPUT: 'Namespace(verbose=3)'
 
# > 'help' - This prints a complete help message for all the options in the current parser and then exits.
# By default a help action is automatically added to the parser. See ArgumentParser for details of how the output is created.
#
# > 'version' - This expects a version= keyword argument in the add_argument() call, and prints version information and exits when invoked:
# 

import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--version', action='version', version='%(prog)s 2.0')

parser.parse_args(['--version'])
