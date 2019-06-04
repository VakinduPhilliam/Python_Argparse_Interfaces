# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Printing a version string:
# Similar to the brief usage string, optparse can also print a version string for your program.
# You have to supply the string as the version argument to OptionParser:
 
parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")
 
# %prog is expanded just like it is in usage. Apart from that, version can contain anything you like.
# When you supply it, optparse automatically adds a --version option to your parser.
# If it encounters this option on the command line, it expands your version string (by replacing %prog), prints it to stdout, and exits.
