# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# OptionParser.set_defaults(dest=value, ...). 
# Set default values for several option destinations at once. Using set_defaults() is the preferred way to set default values for options, since multiple
# options can share the same destination. For example, if several “mode” options all set the same destination, any one of them can set the default, and the
# last one wins:
 
parser.add_option("--advanced", action="store_const",
                  dest="mode", const="advanced",
                  default="novice")    # overridden below

parser.add_option("--novice", action="store_const",
                  dest="mode", const="novice",
                  default="advanced")  # overrides above setting
 
#
# To avoid this confusion, use set_defaults():
# 

parser.set_defaults(mode="advanced")

parser.add_option("--advanced", action="store_const",
                  dest="mode", const="advanced")

parser.add_option("--novice", action="store_const",
                  dest="mode", const="novice")
