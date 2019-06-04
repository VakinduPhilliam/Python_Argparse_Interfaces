# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# FileType objects.
# class argparse.FileType(mode='r', bufsize=-1, encoding=None, errors=None). 
# The FileType factory creates objects that can be passed to the type argument of ArgumentParser.add_argument(). Arguments that have FileType objects as
# their type will open command-line arguments as files with the requested modes, buffer sizes, encodings and error handling:
 
parser = argparse.ArgumentParser()

parser.add_argument('--raw', type=argparse.FileType('wb', 0))
parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))

parser.parse_args(['--raw', 'raw.dat', 'file.txt'])

# OUTPUT: 'Namespace(out=<_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>, raw=<_io.FileIO name='raw.dat' mode='wb'>)'
 
#
# FileType objects understand the pseudo-argument '-' and automatically convert this into sys.stdin for readable FileType objects and sys.stdout for
# writable FileType objects:
#

parser = argparse.ArgumentParser()

parser.add_argument('infile', type=argparse.FileType('r'))
parser.parse_args(['-'])

# OUTPUT: 'Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)'
