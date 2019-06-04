# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Parsing arguments:
# The whole point of creating and populating an OptionParser is to call its parse_args() method:
# 

(options, args) = parser.parse_args(args=None, values=None)
 
# where the input parameters are;
#
# 'args' the list of arguments to process (default: sys.argv[1:]) values an optparse.
# 'Values' object to store option arguments in (default: a new instance of Values) – if you give an existing object, the option defaults will not be
# initialized on it and the return values are;
# options the same object that was passed in as values, or the optparse.Values instance created by optparse args the leftover positional arguments after 
# all options have been processed.