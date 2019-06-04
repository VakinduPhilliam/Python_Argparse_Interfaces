# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
# 
# fromfile_prefix_chars
# Sometimes, for example when dealing with a particularly long argument lists, it may make sense to keep the list of arguments in a file rather than typing
# it out at the command line. If the fromfile_prefix_chars= argument is given to the ArgumentParser constructor, then arguments that start with any of the
# specified characters will be treated as files, and will be replaced by the arguments they contain.
#
# For example:
# 

with open('args.txt', 'w') as fp:
        fp.write('-f\nbar')

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f')

parser.parse_args(['-f', 'foo', '@args.txt'])
