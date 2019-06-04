# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Callback example: fixed arguments.
# Things get slightly more interesting when you define callback options that take a fixed number of arguments.
# Specifying that a callback option takes arguments is similar to defining a "store" or "append" option: if you define type, then the option takes one
# argument that must be convertible to that type; if you further define nargs, then the option takes nargs arguments.
# 
# Here’s an example that just emulates the standard "store" action:
# 

def store_value(option, opt_str, value, parser):
    setattr(parser.values, option.dest, value)

# ...

parser.add_option("--foo",
                  action="callback", callback=store_value,
                  type="int", nargs=3, dest="foo")
