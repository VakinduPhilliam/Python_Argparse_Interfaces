# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Putting it all together
# 
# Here’s what optparse-based scripts usually look like:
# 

from optparse import OptionParser

# ...

def main():

    usage = "usage: %prog [options] arg"

    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")

    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")

    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")

#    ...

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("incorrect number of arguments")

    if options.verbose:
        print("reading %s..." % options.filename)

#    ...

if __name__ == "__main__":

    main()
