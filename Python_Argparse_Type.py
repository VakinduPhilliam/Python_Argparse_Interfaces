# Python argparse
# argparse � Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# type.
# By default, ArgumentParser objects read command-line arguments in as simple strings. However, quite often the command-line string should instead be
# interpreted as another type, like a float or int. The type keyword argument of add_argument() allows any necessary type-checking and type conversions to
# be performed. Common built-in types and functions can be used directly as the value of the type argument:
# 

parser = argparse.ArgumentParser()
parser.add_argument('foo', type=int)

parser.add_argument('bar', type=open)

parser.parse_args('2 temp.txt'.split())

#
# To ease the use of various types of files, the argparse module provides the factory FileType which takes the mode=, bufsize=, encoding= and
# errors= arguments of the open() function. For example, FileType('w') can be used to create a writable file:
# 

parser = argparse.ArgumentParser()
parser.add_argument('bar', type=argparse.FileType('w'))

parser.parse_args(['out.txt'])

# OUTPUT: 'Namespace(bar=<_io.TextIOWrapper name='out.txt' encoding='UTF-8'>)'

# 
# type= can take any callable that takes a single string argument and returns the converted value:
# 

def perfect_square(string):
        value = int(string)
        sqrt = math.sqrt(value)

        if sqrt != int(sqrt):
            msg = "%r is not a perfect square" % string

            raise argparse.ArgumentTypeError(msg)
        return value

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', type=perfect_square)

parser.parse_args(['9'])

# OUTPUT: 'Namespace(foo=9)'

parser.parse_args(['7'])

#
# The choices keyword argument may be more convenient for type checkers that simply check against a range of values:
# 

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', type=int, choices=range(5, 10))

parser.parse_args(['7'])

# OUTPUT: 'Namespace(foo=7)'

parser.parse_args(['11'])
