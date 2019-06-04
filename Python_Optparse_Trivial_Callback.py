# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Callback example: trivial callback
#
# Here’s an example of a callback option that takes no arguments, and simply records that the option was seen:
# 

def record_foo_seen(option, opt_str, value, parser):
    parser.values.saw_foo = True

parser.add_option("--foo", action="callback", callback=record_foo_seen)
