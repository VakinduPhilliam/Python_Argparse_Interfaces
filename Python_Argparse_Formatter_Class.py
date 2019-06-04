# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# formatter_class
# ArgumentParser objects allow the help formatting to be customized by specifying an alternate formatting class. Currently, there are four such classes:
# class argparse.RawDescriptionHelpFormatter class argparse.RawTextHelpFormatter class argparse.ArgumentDefaultsHelpFormatter
# class argparse.MetavarTypeHelpFormatter
# RawDescriptionHelpFormatter and RawTextHelpFormatter give more control over how textual descriptions are displayed.
# By default, ArgumentParser objects line-wrap the description and epilog texts in command-line help messages:
 
parser = argparse.ArgumentParser(
        prog='PROG',
        description='''this description
            was indented weird
                but that is okay''',
        epilog='''
                likewise for this epilog whose whitespace will
            be cleaned up and whose words will be wrapped
            across a couple lines''')

parser.print_help()
