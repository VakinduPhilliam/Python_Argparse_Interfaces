# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Understanding option actions.
# Actions tell optparse what to do when it encounters an option on the command line. There is a fixed set of actions hard-coded into optparse; adding new
# actions is an advanced topic covered in section Extending optparse. Most actions tell optparse to store a value in some variable—for example, take a
# string from the command line and store it in an attribute of options.
# 
# If you don’t specify an option action, optparse defaults to store.
#
# The store action:
# The most common option action is store, which tells optparse to take the next argument (or the remainder of the current argument), ensure that it is of
# the correct type, and store it to your chosen destination.
# 
# For example:
# 

parser.add_option("-f", "--file",
                  action="store", type="string", dest="filename")

# 
# Now let’s make up a fake command line and ask optparse to parse it:
# 

args = ["-f", "foo.txt"]

(options, args) = parser.parse_args(args)
 
#
# When optparse sees the option string -f, it consumes the next argument, foo.txt, and stores it in options.filename.
# So, after this call to parse_args(), options.filename is "foo.txt".
#

# 
# Some other option types supported by optparse are int and float. Here’s an option that expects an integer argument:
# 

parser.add_option("-n", type="int", dest="num")
 
#
# Note that this option has no long option string, which is perfectly acceptable. Also, there’s no explicit action, since the default is store.
#

# 
# Let’s parse another fake command-line. This time, we’ll jam the option argument right up against the option: since -n42 (one argument) is equivalent to
# -n 42 (two arguments), the code
# 

(options, args) = parser.parse_args(["-n42"])

print(options.num)

# 
# will print 42.
#
 
#
# If you don’t specify a type, optparse assumes string. Combined with the fact that the default action is store, that means our first example can be a lot
# shorter:
# 

parser.add_option("-f", "--file", dest="filename")
