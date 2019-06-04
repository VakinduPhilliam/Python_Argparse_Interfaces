# Python Optparse
# optparse � Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
#
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Callback example: variable arguments
# 
# Things get hairy when you want an option to take a variable number of arguments. For this case, you must write a callback, as optparse doesn�t provide any
# built-in capabilities for it.
# And you have to deal with certain intricacies of conventional Unix command-line parsing that optparse normally handles for
# you.
#
# In particular, callbacks should implement the conventional rules for bare -- and - arguments:
#
# > either -- or - can be option arguments
# > bare -- (if not the argument to some option): halt command-line processing and discard the --
# > bare - (if not the argument to some option): halt command-line processing but keep the - (append it to parser.largs)
# 
# If you want an option that takes a variable number of arguments, there are several subtle, tricky issues to worry about.
# The exact implementation you choose will be based on which trade-offs you�re willing to make for your application (which is why optparse doesn�t support
# this sort of thing directly).
# 
# Nevertheless, here�s a stab at a callback for an option with variable arguments:
# 

def vararg_callback(option, opt_str, value, parser):
    assert value is None

    value = []

    def floatable(str):

        try:
            float(str)
            return True

        except ValueError:
            return False

    for arg in parser.rargs:

        # stop on --foo like options

        if arg[:2] == "--" and len(arg) > 2:
            break

        # stop on -a, but not on -3 or -3.0

        if arg[:1] == "-" and len(arg) > 1 and not floatable(arg):
            break

        value.append(arg)

    del parser.rargs[:len(value)]

    setattr(parser.values, option.dest, value)

# ...

parser.add_option("-c", "--callback", dest="vararg_attr",
                  action="callback", callback=vararg_callback)
