# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# conflict_handler
# ArgumentParser objects do not allow two actions with the same option string. By default, ArgumentParser objects raise an exception if an attempt is made
# to create an argument with an option string that is already in use:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-f', '--foo', help='old foo help')

parser.add_argument('--foo', help='new foo help')

#
# OUTPUT:
#
# Traceback (most recent call last):
# ..
# ArgumentError: argument --foo: conflicting option string(s): --foo
 
#
# Sometimes (e.g. when using parents) it may be useful to simply override any older arguments with the same option string.
# To get this behavior, the value 'resolve' can be supplied to the conflict_handler= argument of ArgumentParser:
# 

parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
parser.add_argument('-f', '--foo', help='old foo help')

parser.add_argument('--foo', help='new foo help')

parser.print_help()
