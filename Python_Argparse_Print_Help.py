# Python argparse
# argparse � Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# help:
# The help value is a string containing a brief description of the argument. When a user requests help (usually by using -h or --help at the command line), 
# these help descriptions will be displayed with each argument:
# 

parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('--foo', action='store_true',
                        help='foo the bars before frobbling')

parser.add_argument('bar', nargs='+',
                        help='one of the bars to be frobbled')

parser.parse_args(['-h'])

#
# The help strings can include various format specifiers to avoid repetition of things like the program name or the argument default.
# The available specifiers include the program name, %(prog)s and most keyword arguments to add_argument(), e.g. %(default)s, %(type)s, etc.:
# 

parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('bar', nargs='?', type=int, default=42,
                        help='the bar to %(prog)s (default: %(default)s)')

parser.print_help()

#
# As the help string supports %-formatting, if you want a literal % to appear in the help string, you must escape it as %%.
# argparse supports silencing the help entry for certain options, by setting the help value to argparse.SUPPRESS:
# 

parser = argparse.ArgumentParser(prog='frobble')
parser.add_argument('--foo', help=argparse.SUPPRESS)

parser.print_help()
