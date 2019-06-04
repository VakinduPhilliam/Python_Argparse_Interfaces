# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Default values.
# 
# All of the above examples involve setting some variable (the “destination”) when certain command-line options are seen. What happens if those options are
# never seen? Since we didn’t supply any defaults, they are all set to None.
# This is usually fine, but sometimes you want more control. optparse lets you supply a default value for each destination, which is assigned before the
# command line is parsed.
# First, consider the verbose/quiet example. If we want optparse to set verbose to True unless -q is seen, then we can do this:
 
parser.add_option("-v", action="store_true", dest="verbose", default=True)
parser.add_option("-q", action="store_false", dest="verbose")

# 
# Since default values apply to the destination rather than to any particular option, and these two options happen to have the same destination, this is 
# exactly equivalent:
# 

parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-q", action="store_false", dest="verbose", default=True)

# 
# Consider this:
# 

parser.add_option("-v", action="store_true", dest="verbose", default=False)
parser.add_option("-q", action="store_false", dest="verbose", default=True)

# 
# Again, the default value for verbose will be True: the last default value supplied for any particular destination is the one that counts.
#

# 
# A clearer way to specify default values is the set_defaults() method of OptionParser, which you can call at any time before calling parse_args():
# 

parser.set_defaults(verbose=True)

parser.add_option(...)

(options, args) = parser.parse_args()
