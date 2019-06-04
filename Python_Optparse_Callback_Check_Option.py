# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Callback example: check option order (generalized)
# 
# If you want to re-use this callback for several similar options (set a flag, but blow up if -b has already been seen), it needs a bit of work: the error
# message and the flag that it sets must be generalized.
# 

def check_order(option, opt_str, value, parser):

    if parser.values.b:
        raise OptionValueError("can't use %s after -b" % opt_str)

    setattr(parser.values, option.dest, 1)

# ...

parser.add_option("-a", action="callback", callback=check_order, dest='a')
parser.add_option("-b", action="store_true", dest="b")

parser.add_option("-c", action="callback", callback=check_order, dest='c')
