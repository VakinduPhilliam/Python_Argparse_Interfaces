# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
#
# Parents
# Sometimes, several parsers share a common set of arguments. Rather than repeating the definitions of these arguments, a single parser with all the shared
# arguments and passed to parents= argument to ArgumentParser can be used. The parents= argument takes a list of ArgumentParser objects, collects all the
# positional and optional actions from them, and adds these actions to the ArgumentParser object being constructed:
# 

parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent', type=int)

foo_parser = argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('foo')

foo_parser.parse_args(['--parent', '2', 'XXX'])

# OUTPUT: 'Namespace(foo='XXX', parent=2)'

bar_parser = argparse.ArgumentParser(parents=[parent_parser])
bar_parser.add_argument('--bar')

bar_parser.parse_args(['--bar', 'YYY'])

# OUTPUT: 'Namespace(bar='YYY', parent=None)'
