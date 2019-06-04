# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Populating the parser.
# 
# There are several ways to populate the parser with options. The preferred way is by using OptionParser.add_option().
# add_option() can be called in one of two ways:
#
# > pass it an Option instance (as returned by make_option())
# > pass it any combination of positional and keyword arguments that are acceptable to make_option() (i.e., to the Option constructor), and it will create
#   the Option instance for you
#

# 
# The other alternative is to pass a list of pre-constructed Option instances to the OptionParser constructor, as in:
# 

option_list = [
    make_option("-f", "--filename",
                action="store", type="string", dest="filename"),

    make_option("-q", "--quiet",
                action="store_false", dest="verbose"),
    ]

parser = OptionParser(option_list=option_list)
