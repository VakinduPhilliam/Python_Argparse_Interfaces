# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# required
# In general, the argparse module assumes that flags like -f and --bar indicate optional arguments, which can always be omitted at the command line.
# To make an option required, True can be specified for the required= keyword argument to add_argument():
 
parser = argparse.ArgumentParser()
parser.add_argument('--foo', required=True)

parser.parse_args(['--foo', 'BAR'])

# OUTPUT: 'Namespace(foo='BAR')'

parser.parse_args([])

#
# As the example shows, if an option is marked as required, parse_args() will report an error if that option is not present at the command line.
#