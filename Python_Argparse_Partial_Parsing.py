# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Partial parsing.
# ArgumentParser.parse_known_args(args=None, namespace=None). 
#
# Sometimes a script may only parse a few of the command-line arguments, passing the remaining arguments on to another script or program.
# In these cases, the parse_known_args() method can be useful. It works much like parse_args() except that it does not produce an error when extra arguments
# are present.
# Instead, it returns a two item tuple containing the populated namespace and the list of remaining argument strings.
# 

parser = argparse.ArgumentParser()

parser.add_argument('--foo', action='store_true')
parser.add_argument('bar')

parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
