# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# You may also specify an arbitrary action by passing an Action subclass or other object that implements the same interface.
# The recommended way to do this is to extend Action, overriding the __call__ method and optionally the __init__ method.
# 
# An example of a custom action:
# 

class FooAction(argparse.Action):

        def __init__(self, option_strings, dest, nargs=None, **kwargs):

            if nargs is not None:
                raise ValueError("nargs not allowed")

                super(FooAction, self).__init__(option_strings, dest, **kwargs)

        def __call__(self, parser, namespace, values, option_string=None):

            print('%r %r %r' % (namespace, values, option_string))

            setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action=FooAction)

parser.add_argument('bar', action=FooAction)

args = parser.parse_args('1 --foo 2'.split())

# OUTPUT: 'Namespace(bar=None, foo=None) '1' None'
# OUTPUT: 'Namespace(bar='1', foo=None) '2' '--foo'

args

# OUTPUT: 'Namespace(bar='1', foo='2')'
