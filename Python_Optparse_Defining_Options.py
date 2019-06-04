# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Defining options.
# Each Option instance represents a set of synonymous command-line option strings, e.g. -f and --file.
# You can specify any number of short or long option strings, but you must specify at least one overall option string.
#
# The canonical way to create an Option instance is with the add_option() method of OptionParser.
# OptionParser.add_option(option) OptionParser.add_option(*opt_str, attr=value, ...)
# To define an option with only a short option string:
# 

parser.add_option("-f", attr=value, ...)

# 
# And to define an option with only a long option string:
# 

parser.add_option("--foo", attr=value, ...)

# Most actions involve storing or updating a value somewhere.
# optparse always creates a special object for this, conventionally called options (it happens to be an instance of optparse.Values). 
# Option arguments (and various other values) are stored as attributes of this object, according to the dest (destination) option attribute.

# 
# For example, when you call,
# 

parser.parse_args()
 
#
# one of the first things optparse does is create the options object:
# 

options = Values()
 
#
# If one of the options in this parser is defined with,
# 

parser.add_option("-f", "--file", action="store", type="string", dest="filename")
 
#
# and the command-line being parsed includes any of the following:
#

# -ffoo
# -f foo
# --file=foo
# --file foo
 
#
# then optparse, on seeing this option, will do the equivalent of
# 

options.filename = "foo"

#
# The type and dest option attributes are almost as important as action, but action is the only one that makes sense for all options.
#
