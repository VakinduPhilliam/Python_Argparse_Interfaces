# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Generating help:
# optparse’s ability to generate help and usage text automatically is useful for creating user-friendly command-line interfaces.
# All you have to do is supply a help value for each option, and optionally a short usage message for your whole program.
#
# Here’s an OptionParser populated with user-friendly (documented) options:
#
 
usage = "usage: %prog [options] arg1 arg2"

parser = OptionParser(usage=usage)

parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=True,
                  help="make lots of noise [default]")

parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose",
                  help="be vewwy quiet (I'm hunting wabbits)")

parser.add_option("-f", "--filename",
                  metavar="FILE", help="write output to FILE")

parser.add_option("-m", "--mode",
                  default="intermediate",
                  help="interaction mode: novice, intermediate, "
                       "or expert [default: %default]")

#
# A bit more complete example might involve using more than one group: still extending the previous example:
# 

group = OptionGroup(parser, "Dangerous Options",
                    "Caution: use these options at your own risk.  "
                    "It is believed that some of them bite.")

group.add_option("-g", action="store_true", help="Group option.")
parser.add_option_group(group)

group = OptionGroup(parser, "Debug Options")
group.add_option("-d", "--debug", action="store_true",
                 help="Print debug information")

group.add_option("-s", "--sql", action="store_true",
                 help="Print all SQL statements executed")

group.add_option("-e", action="store_true", help="Print every action done")

parser.add_option_group(group)
