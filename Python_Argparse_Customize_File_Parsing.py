# Python argparse
# argparse — Parser for command-line options, arguments and sub-commands.
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
#
# Customizing file parsing
# ArgumentParser.convert_arg_line_to_args(arg_line) 
# Arguments that are read from a file (see the fromfile_prefix_chars keyword argument to the ArgumentParser constructor) are read one argument per line.
# convert_arg_line_to_args() can be overridden for fancier reading.
# 
# This method takes a single argument arg_line which is a string read from the argument file. It returns a list of arguments parsed from this string.
# The method is called once per line read from the argument file, in order.
# A useful override of this method is one that treats each space-separated word as an argument. The following example demonstrates how to do this:
# 

class MyArgumentParser(argparse.ArgumentParser):

    def convert_arg_line_to_args(self, arg_line):

        return arg_line.split()
