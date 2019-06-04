# Python argparse
# argparse � Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# nargs.
# ArgumentParser objects usually associate a single command-line argument with a single action to be taken.
# The nargs keyword argument associates a different number of command-line arguments with a single action. The supported values are:
# N (an integer). N arguments from the command line will be gathered together into a list.
#
# For example:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs=2)

parser.add_argument('bar', nargs=1)

parser.parse_args('c --foo a b'.split())

# OUTPUT: 'Namespace(bar=['c'], foo=['a', 'b'])'

# > '?'. One argument will be consumed from the command line if possible, and produced as a single item. If no command-line argument is present, the value
# from default will be produced. Note that for optional arguments, there is an additional case - the option string is present but not followed by a
# command-line argument. In this case the value from const will be produced.
#
# Some examples to illustrate this:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?', const='c', default='d')

parser.add_argument('bar', nargs='?', default='d')
parser.parse_args(['XX', '--foo', 'YY'])

# OUTPUT: 'Namespace(bar='XX', foo='YY')'

parser.parse_args(['XX', '--foo'])

# OUTPUT: 'Namespace(bar='XX', foo='c')'

parser.parse_args([])

# OUTPUT: 'Namespace(bar='d', foo='d')'

# 
# One of the more common uses of nargs='?' is to allow optional input and output files:
# 

parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)

parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)

parser.parse_args(['input.txt', 'output.txt'])

#
# OUTPUT:
#
# 'Namespace(infile=<_io.TextIOWrapper name='input.txt' encoding='UTF-8'>,
#          outfile=<_io.TextIOWrapper name='output.txt' encoding='UTF-8'>)

parser.parse_args([])

#
# OUTPUT:
#
# Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>,
#          outfile=<_io.TextIOWrapper name='<stdout>' encoding='UTF-8'>)
 
#
# > '*'. All command-line arguments present are gathered into a list. Note that it generally doesn�t make much sense to have more than one positional
# argument with nargs='*', but multiple optional arguments with nargs='*' is possible.
#
# For example:
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='*')

parser.add_argument('--bar', nargs='*')

parser.add_argument('baz', nargs='*')

parser.parse_args('a b --foo x y --bar 1 2'.split())

# OUTPUT: 'Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])'
 
# > '+'. Just like '*', all command-line args present are gathered into a list. Additionally, an error message will be generated if there wasn�t at least
# one command-line argument present.
#
# For example:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', nargs='+')

parser.parse_args(['a', 'b'])

# OUTPUT: 'Namespace(foo=['a', 'b'])'

parser.parse_args([])

#
# > argparse.REMAINDER. All the remaining command-line arguments are gathered into a list.
# This is commonly useful for command line utilities that dispatch to other command line utilities:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo')

parser.add_argument('command')

parser.add_argument('args', nargs=argparse.REMAINDER)

print(parser.parse_args('--foo B cmd --arg1 XX ZZ'.split()))

# OUTPUT: 'Namespace(args=['--arg1', 'XX', 'ZZ'], command='cmd', foo='B')'

# 
# If the nargs keyword argument is not provided, the number of arguments consumed is determined by the action. Generally this means a single command-line
# argument will be consumed and a single item (not a list) will be produced.
#
