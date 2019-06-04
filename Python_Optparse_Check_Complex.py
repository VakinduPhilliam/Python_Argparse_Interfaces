# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# A silly example that demonstrates adding a "complex" option type to parse Python-style complex numbers on the command line.
# (This is even sillier than it used to be, because optparse 1.3 added built-in support for complex numbers, but never mind.)
# 
# First, the necessary imports:
# 

from copy import copy
from optparse import Option, OptionValueError
 
#
# You need to define your type-checker first, since it’s referred to later (in the TYPE_CHECKER class attribute of your Option subclass):
# 

def check_complex(option, opt, value):

    try:
        return complex(value)

    except ValueError:
        raise OptionValueError(
            "option %s: invalid complex value: %r" % (opt, value))
 
#
# Finally, the Option subclass:
# 

class MyOption (Option):

    TYPES = Option.TYPES + ("complex",)

    TYPE_CHECKER = copy(Option.TYPE_CHECKER)

    TYPE_CHECKER["complex"] = check_complex

#
# That’s it! Now you can write a script that uses the new option type just like any other optparse-based script, except you have to instruct your
# OptionParser to use MyOption instead of Option:
# 

parser = OptionParser(option_class=MyOption)
parser.add_option("-c", type="complex")
 
#
# Alternately, you can build your own option list and pass it to OptionParser; if you don’t use add_option() in the above way, you don’t need to tell
# OptionParser which option class to use:
# 

option_list = [MyOption("-c", action="store", type="complex", dest="c")]

parser = OptionParser(option_list=option_list)
