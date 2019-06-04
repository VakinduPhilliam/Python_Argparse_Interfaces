# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Conflicts between options.
# If you’re not careful, it’s easy to define options with conflicting option strings:
 
parser.add_option("-n", "--dry-run", ...)

# ...

parser.add_option("-n", "--noisy", ...)
 
# (This is particularly true if you’ve defined your own OptionParser subclass with some standard options.)
# Every time you add an option, optparse checks for conflicts with existing options. If it finds any, it invokes the current conflict-handling mechanism.
# You can set the conflict-handling mechanism either in the constructor: 

parser = OptionParser(..., conflict_handler=handler)
 
#
# or with a separate call:
# 

parser.set_conflict_handler(handler)
 
#
# The available conflict handlers are:
# "error" (default) assume option conflicts are a programming error and raise OptionConflictError "resolve" resolve option conflicts intelligently.
# As an example, let’s define an OptionParser that resolves conflicts intelligently and add conflicting options to it:
 
parser = OptionParser(conflict_handler="resolve")

parser.add_option("-n", "--dry-run", ..., help="do no harm")
parser.add_option("-n", "--noisy", ..., help="be noisy")
 
#
# At this point, optparse detects that a previously-added option is already using the -n option string. Since conflict_handler is "resolve", it resolves the
# situation by removing -n from the earlier option’s list of option strings. Now --dry-run is the only way for the user to activate that option.
# If the user asks for help, the help message will reflect that:
# 

#
# It’s possible to whittle away the option strings for a previously-added option until there are none left, and the user has no way of invoking that option
# from the command-line. In that case, optparse removes that option completely, so it doesn’t show up in help text or anywhere else.
# Carrying on with our existing OptionParser:
# 

parser.add_option("--dry-run", ..., help="new dry-run option")
