# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Handling boolean (flag) options.
# Flag options—set a variable to true or false when a particular option is seen—are quite common. optparse supports them with two separate actions,
# store_true and store_false. For example, you might have a verbose flag that is turned on with -v and off with -q:
# 

parser.add_option("-v", action="store_true", dest="verbose")

parser.add_option("-q", action="store_false", dest="verbose")
