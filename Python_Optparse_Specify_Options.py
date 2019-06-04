# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# While optparse is quite flexible and powerful, it’s also straightforward to use in most cases.
# This script covers the code patterns that are common to any optparse-based program.
#

#
# First, you need to import the OptionParser class; then, early in the main program, create an OptionParser instance:
# 

from optparse import OptionParser

# ...

parser = OptionParser()
 
#
# Then you can start defining options.
# The basic syntax is:
# 

parser.add_option(opt_str, ...,
                  attr=value, ...)

# 
# Each option has one or more option strings, such as -f or --file, and several option attributes that tell optparse what to expect and what to do when it
# encounters that option on the command line.
#

# 
# Typically, each option will have one short option string and one long option string, e.g.:
# 

parser.add_option("-f", "--file", ...)

# 
# You’re free to define as many short option strings and as many long option strings as you like (including zero), as long as there is at least one option
# string overall.
#
 
#
# The option strings passed to OptionParser.add_option() are effectively labels for the option defined by that call. For brevity, we will frequently refer
# to encountering an option on the command line; in reality, optparse encounters option strings and looks up options from them.
# 

#
# Once all of your options are defined, instruct optparse to parse your program’s command line:
# 

(options, args) = parser.parse_args()

