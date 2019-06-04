# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# How optparse handles errors
# There are two broad classes of errors that optparse has to worry about: programmer errors and user errors. Programmer errors are usually erroneous calls
# to OptionParser.add_option(), e.g. invalid option strings, unknown option attributes, missing option attributes, etc.
# These are dealt with in the usual way: raise an exception (either optparse.OptionError or TypeError) and let the program crash.
# Handling user errors is much more important, since they are guaranteed to happen no matter how stable your code is. optparse can automatically detect some
# user errors, such as bad option arguments (passing -n 4x where -n takes an integer argument), missing arguments (-n at the end of the command line,
# where -n takes an argument of any type). Also, you can call OptionParser.error() to signal an application-defined error condition:
# 

(options, args) = parser.parse_args()

# ...

if options.a and options.b:

    parser.error("options -a and -b are mutually exclusive")
 
#
# In either case, optparse handles the error the same way: it prints the program’s usage message and an error message to standard error and exits with error
# status 2.
#