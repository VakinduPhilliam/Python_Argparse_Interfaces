# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Defining a callback option.
# As always, the easiest way to define a callback option is by using the OptionParser.add_option() method. Apart from action, the only option attribute you
# must specify is callback, the function to call:
# 

parser.add_option("-c", action="callback", callback=my_callback)
 
#
# callback is a function (or other callable object), so you must have already defined my_callback() when you create this callback option.
# In this simple case, optparse doesn’t even know if -c takes any arguments, which usually means that the option takes no arguments—the mere presence of -c
# on the command-line is all it needs to know. In some circumstances, though, you might want your callback to consume an arbitrary number of command-line
# arguments.
# 
# optparse always passes four particular arguments to your callback, and it will only pass additional arguments if you specify them via callback_args and
# callback_kwargs. Thus, the minimal callback function signature is:
# 

def my_callback(option, opt, value, parser):
