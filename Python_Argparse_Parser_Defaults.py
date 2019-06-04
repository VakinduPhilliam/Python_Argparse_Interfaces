# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Parser defaults.
# ArgumentParser.set_defaults(**kwargs). 
# Most of the time, the attributes of the object returned by parse_args() will be fully determined by inspecting the command-line arguments and the argument
# actions.
# set_defaults() allows some additional attributes that are determined without any inspection of the command line to be added:
# 

parser = argparse.ArgumentParser()

parser.add_argument('foo', type=int)
parser.set_defaults(bar=42, baz='badger')

parser.parse_args(['736'])

# OUTPUT: 'Namespace(bar=42, baz='badger', foo=736)'

# 
# Note that parser-level defaults always override argument-level defaults:
# 

parser = argparse.ArgumentParser()

parser.add_argument('--foo', default='bar')
parser.set_defaults(foo='spam')

parser.parse_args([])

# OUTPUT: 'Namespace(foo='spam')'

# 
# Parser-level defaults can be particularly useful when working with multiple parsers. See the add_subparsers() method for an example of this type.
# ArgumentParser.get_default(dest) 
# Get the default value for a namespace attribute, as set by either add_argument() or by set_defaults():
# 

parser = argparse.ArgumentParser()

parser.add_argument('--foo', default='badger')
parser.get_default('foo')

# OUTPUT: 'badger'
