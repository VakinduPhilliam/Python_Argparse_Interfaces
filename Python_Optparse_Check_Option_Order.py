# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Callback example: check option order
# 
# Here’s a slightly more interesting example: record the fact that -a is seen, but blow up if it comes after -b in the command-line.
# 

def check_order(option, opt_str, value, parser):

    if parser.values.b:
        raise OptionValueError("can't use -a after -b")

    parser.values.a = 1

# ...

parser.add_option("-a", action="callback", callback=check_order)

parser.add_option("-b", action="store_true", dest="b")
