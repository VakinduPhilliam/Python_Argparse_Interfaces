# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Argument groups.
# ArgumentParser.add_argument_group(title=None, description=None). 
# By default, ArgumentParser groups command-line arguments into “positional arguments” and “optional arguments” when displaying help messages.
# When there is a better conceptual grouping of arguments than this default one, appropriate groups can be created using the add_argument_group() method:
# 

parser = argparse.ArgumentParser(prog='PROG', add_help=False)

group = parser.add_argument_group('group')
group.add_argument('--foo', help='foo help')

group.add_argument('bar', help='bar help')

#
# The add_argument_group() method returns an argument group object which has an add_argument() method just like a regular ArgumentParser.
# When an argument is added to the group, the parser treats it just like a normal argument, but displays the argument in a separate group for help messages.
# The add_argument_group() method accepts title and description arguments which can be used to customize this display:
# 

parser = argparse.ArgumentParser(prog='PROG', add_help=False)

group1 = parser.add_argument_group('group1', 'group1 description')
group1.add_argument('foo', help='foo help')

group2 = parser.add_argument_group('group2', 'group2 description')
group2.add_argument('--bar', help='bar help')

parser.print_help()

