# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Grouping Options
# When dealing with many options, it is convenient to group these options for better help output. An OptionParser can contain several option groups, each of which can contain several options.
#
# An option group is obtained using the class OptionGroup:
# class optparse.OptionGroup(parser, title, description=None) 
# where;
#
# > parser is the OptionParser instance the group will be inserted in to
# > title is the group title
# > description, optional, is a long description of the group
# 
# OptionGroup inherits from OptionContainer (like OptionParser) and so the add_option() method can be used to add an option to the group.
# Once all the options are declared, using the OptionParser method add_option_group() the group is added to the previously defined parser.
# Continuing with the parser defined in the previous section, adding an OptionGroup to a parser is easy:
# 

group = OptionGroup(parser, "Dangerous Options",
                    "Caution: use these options at your own risk.  "
                    "It is believed that some of them bite.")

group.add_option("-g", action="store_true", help="Group option.")

parser.add_option_group(group)
