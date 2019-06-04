# Python Optparse
# optparse � Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Standard option actions.
# The various option actions all have slightly different requirements and effects.
# Most actions have several relevant option attributes which you may specify to guide optparse�s behaviour; a few have required attributes, which you must
# specify for any option using that action.
#  > "store" [relevant: type, dest, nargs, choices]
# The option must be followed by an argument, which is converted to a value according to type and stored in dest. If nargs > 1, multiple arguments will be
# consumed from the command line; all will be converted according to type and stored to dest as a tuple. See the Standard option types section.
# If choices is supplied (a list or tuple of strings), the type defaults to "choice".
# If type is not supplied, it defaults to "string".
# If dest is not supplied, optparse derives a destination from the first long option string (e.g., --foo-bar implies foo_bar). If there are no long option
# strings, optparse derives a destination from the first short option string (e.g., -f implies f).
# 
# Example:
# 

parser.add_option("-f")
parser.add_option("-p", type="float", nargs=3, dest="point")
 
#
# As it parses the command line,
# 

# -f foo.txt -p 1 -3.5 4 -fbar.txt

# 
# optparse will set
# 

options.f = "foo.txt"
options.point = (1.0, -3.5, 4.0)
options.f = "bar.txt"
 
# > "store_const" [required: const; relevant: dest]
# 
# The value const is stored in dest.
#
# 
# Example:
# 

parser.add_option("-q", "--quiet",
                  action="store_const", const=0, dest="verbose")

parser.add_option("-v", "--verbose",
                  action="store_const", const=1, dest="verbose")

parser.add_option("--noisy",
                  action="store_const", const=2, dest="verbose")
 
#
# If --noisy is seen, optparse will set
# 

options.verbose = 2

# 
# > "store_true" [relevant: dest]
#

# 
# A special case of "store_const" that stores a true value to dest.
# 

# > "store_false" [relevant: dest]
 
# 
# Like "store_true", but stores a false value.
#

# 
# Example:
# 

parser.add_option("--clobber", action="store_true", dest="clobber")
parser.add_option("--no-clobber", action="store_false", dest="clobber")
 
#
# > "append" [relevant: type, dest, nargs, choices]
#

# 
# The option must be followed by an argument, which is appended to the list in dest. If no default value for dest is supplied, an empty list is automatically
# created when optparse first encounters this option on the command-line. If nargs > 1, multiple arguments are consumed, and a tuple of length nargs is
# appended to dest.
#
 
#
# The defaults for type and dest are the same as for the "store" action.
#
 
#
# Example:
# 

parser.add_option("-t", "--tracks", action="append", type="int")
 
#
# If -t3 is seen on the command-line, optparse does the equivalent of:
# 

options.tracks = []
options.tracks.append(int("3"))

# 
# If, a little later on, --tracks=4 is seen, it does:
# 

options.tracks.append(int("4"))
 
#
# The append action calls the append method on the current value of the option. This means that any default value specified must have an append method.
# It also means that if the default value is non-empty, the default elements will be present in the parsed value for the option, with any values from the
# command line appended after those default values:
# 

parser.add_option("--files", action="append", default=['~/.mypkg/defaults'])

opts, args = parser.parse_args(['--files', 'overrides.mypkg'])
opts.files

# OUTPUT: '['~/.mypkg/defaults', 'overrides.mypkg']'
 
# > "append_const" [required: const; relevant: dest]
# Like "store_const", but the value const is appended to dest; as with "append", dest defaults to None, and an empty list is automatically created the first
# time the option is encountered.
# "count" [relevant: dest]
# Increment the integer stored at dest. If no default value is supplied, dest is set to zero before being incremented the first time.
# 
# Example:
# 

parser.add_option("-v", action="count", dest="verbosity")
 
#
# The first time -v is seen on the command line, optparse does the equivalent of:
# 

options.verbosity = 0
options.verbosity += 1
 
#
# Every subsequent occurrence of -v results in
# 

options.verbosity += 1
 
#
# "callback" [required: callback; relevant: type, nargs, callback_args, callback_kwargs]
#

# 
# Call the function specified by callback, which is called as
# 

func(option, opt_str, value, parser, *args, **kwargs)
 

# > "help"
# Prints a complete help message for all the options in the current option parser. The help message is constructed from the usage string passed to
# OptionParser�s constructor and the help string passed to every option.
# If no help string is supplied for an option, it will still be listed in the help message. To omit an option entirely, use the special value
# optparse.SUPPRESS_HELP.
# optparse automatically adds a help option to all OptionParsers, so you do not normally need to create one.
# 
# Example:
# 

from optparse import OptionParser, SUPPRESS_HELP

# usually, a help option is added automatically, but that can
# be suppressed using the add_help_option argument

parser = OptionParser(add_help_option=False)

parser.add_option("-h", "--help", action="help")

parser.add_option("-v", action="store_true", dest="verbose",
                  help="Be moderately verbose")

parser.add_option("--file", dest="filename",
                  help="Input file to read data from")

parser.add_option("--secret", help=SUPPRESS_HELP)
 
#
# If optparse sees either -h or --help on the command line, it will print something like the following help message to stdout (assuming sys.argv[0] is
# "foo.py"):
# 
