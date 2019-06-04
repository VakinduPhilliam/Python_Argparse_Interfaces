# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# The Namespace object.
# class argparse.Namespace. 
# Simple class used by default by parse_args() to create an object holding attributes and return it.
# 
# This class is deliberately simple, just an object subclass with a readable string representation. If you prefer to have dict-like view of the attributes,
# you can use the standard Python idiom, vars():
# 

parser = argparse.ArgumentParser()
parser.add_argument('--foo')

args = parser.parse_args(['--foo', 'BAR'])

vars(args)

# OUTPUT: '{'foo': 'BAR'}'
 
#
# It may also be useful to have an ArgumentParser assign attributes to an already existing object, rather than a new Namespace object.
# This can be achieved by specifying the namespace= keyword argument:
# 

class C:
        pass

c = C()

parser = argparse.ArgumentParser()
parser.add_argument('--foo')

parser.parse_args(args=['--foo', 'BAR'], namespace=c)

c.foo

# OUTPUT: 'BAR'
