# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Callback example: check arbitrary condition.
# Of course, you could put any condition in there—you’re not limited to checking the values of already-defined options.
#
# For example, if you have options that should not be called when the moon is full, all you have to do is this:
# 

def check_moon(option, opt_str, value, parser):

    if is_moon_full():
        raise OptionValueError("%s option invalid when moon is full"
                               % opt_str)

    setattr(parser.values, option.dest, 1)

# ...

parser.add_option("--foo",
                  action="callback", callback=check_moon, dest="foo")
