# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Sub-commands
#
# ArgumentParser.add_subparsers([title][, description][, prog][, parser_class][, action][, option_string][, dest][, required][, help][, metavar])
# Many programs split up their functionality into a number of sub-commands, for example, the svn program can invoke sub-commands like svn checkout, svn
# update, and svn commit. Splitting up functionality this way can be a particularly good idea when a program performs several different functions which
# require different kinds of command-line arguments.
#
# ArgumentParser supports the creation of such sub-commands with the add_subparsers() method.
# The add_subparsers() method is normally called with no arguments and returns a special action object.
# This object has a single method, add_parser(), which takes a command name and any ArgumentParser constructor arguments, and returns an ArgumentParser
# object that can be modified as usual.
# 
# Description of parameters:
#
# > title - title for the sub-parser group in help output; by default “subcommands” if description is provided, otherwise uses title for positional
#   arguments
# > description - description for the sub-parser group in help output, by default None
# > prog - usage information that will be displayed with sub-command help, by default the name of the program and any positional arguments before the
#    subparser argument
# > parser_class - class which will be used to create sub-parser instances, by default the class of the current parser (e.g. ArgumentParser)
# > action - the basic type of action to be taken when this argument is encountered at the command line
# > dest - name of the attribute under which sub-command name will be stored; by default None and no value is stored
# > required - Whether or not a subcommand must be provided, by default False.
# > help - help for sub-parser group in help output, by default None
# > metavar - string presenting available sub-commands in help; by default it is None and presents sub-commands in form {cmd1, cmd2, ..}
# 
# Some example usage:
# 

# create the top-level parser

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')

subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for the "a" command

parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command

parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

# parse some argument lists

parser.parse_args(['a', '12'])

# OUTPUT: 'Namespace(bar=12, foo=False)'

parser.parse_args(['--foo', 'b', '--baz', 'Z'])

# OUTPUT: 'Namespace(baz='Z', foo=True)'

#
# Similarly, when a help message is requested from a subparser, only the help for that particular parser will be printed.
# The help message will not include parent parser or sibling parser messages. (A help message for each subparser command, however, can be given by supplying
# the help= argument to add_parser() as above.)
# 

parser.parse_args(['--help'])


parser.parse_args(['a', '--help'])


parser.parse_args(['b', '--help'])

#
# The add_subparsers() method also supports title and description keyword arguments. When either is present, the subparser’s commands will appear in their
# own group in the help output.
#
# For example:
# 

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands',
                                       help='additional help')

subparsers.add_parser('foo')
subparsers.add_parser('bar')

parser.parse_args(['-h'])

# 
# Furthermore, add_parser supports an additional aliases argument, which allows multiple strings to refer to the same subparser.
#
# This example, like svn, aliases co as a shorthand for checkout:
# 

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

checkout = subparsers.add_parser('checkout', aliases=['co'])
checkout.add_argument('foo')

parser.parse_args(['co', 'bar'])

# OUTPUT: 'Namespace(foo='bar')'

# 
# One particularly effective way of handling sub-commands is to combine the use of the add_subparsers() method with calls to set_defaults() so that each
# subparser knows which Python function it should execute.
#
# For example:
# 

# sub-command functions

def foo(args):
        print(args.x * args.y)

def bar(args):
        print('((%s))' % args.z)

# create the top-level parser

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "foo" command

parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)

parser_foo.add_argument('y', type=float)

parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command

parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')

parser_bar.set_defaults(func=bar)

# parse the args and call whatever function was selected

args = parser.parse_args('foo 1 -x 2'.split())
args.func(args)

# OUTPUT: '2.0'

# parse the args and call whatever function was selected

args = parser.parse_args('bar XYZYX'.split())
args.func(args)

# OUTPUT: '((XYZYX))'

# 
# This way, you can let parse_args() do the job of calling the appropriate function after argument parsing is complete.
# Associating functions with actions like this is typically the easiest way to handle the different actions for each of your subparsers.
# However, if it is necessary to check the name of the subparser that was invoked, the dest keyword argument to the add_subparsers() call will work:
# 

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest='subparser_name')

subparser1 = subparsers.add_parser('1')
subparser1.add_argument('-x')

subparser2 = subparsers.add_parser('2')
subparser2.add_argument('y')

parser.parse_args(['2', 'frobble'])

# OUTPUT: 'Namespace(subparser_name='2', y='frobble')'
