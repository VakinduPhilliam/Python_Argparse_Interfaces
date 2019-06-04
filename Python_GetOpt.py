# Python GetOpt
# getopt — C-style parser for command line options
# This module helps scripts to parse the command line arguments in sys.argv.
# It supports the same conventions as the Unix getopt() function (including the special meanings of arguments of the form ‘-‘ and ‘--‘).
# Long options similar to those supported by GNU software may be used as well via an optional third argument.
#
# exception getopt.GetoptError: 
# This is raised when an unrecognized option is found in the argument list or when an option requiring an argument is given none.
# The argument to the exception is a string indicating the cause of the error. For long options, an argument given to an option which does not require one
# will also cause this exception to be raised. The attributes msg and opt give the error message and related option; if there is no specific option to which
# the exception relates, opt is an empty string.
#
# exception getopt.error: 
# Alias for GetoptError; for backward compatibility.
# 
# An example using only Unix style options:
# 

import getopt

args = '-a -b -cfoo -d bar a1 a2'.split()
args

optlist, args = getopt.getopt(args, 'abc:d:')
optlist

args

#
# Using long option names is equally easy:
# 

s = '--condition=foo --testing --output-file abc.def -x a1 a2'
args = s.split()

args

optlist, args = getopt.getopt(args, 'x', [
        'condition=', 'output-file=', 'testing'])

optlist

args

# OUTPUT: '['a1', 'a2']'
 
#
# In a script, typical usage is something like this:
# 

import getopt, sys

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])

    except getopt.GetoptError as err:

        # print help information and exit:

        print(err)  # will print something like "option -a not recognized"

        usage()

        sys.exit(2)

    output = None

    verbose = False

    for o, a in opts:

        if o == "-v":
            verbose = True

        elif o in ("-h", "--help"):
            usage()
            sys.exit()

        elif o in ("-o", "--output"):
            output = a

        else:
            assert False, "unhandled option"

    # ...

if __name__ == "__main__":
    main()

#
# Note that an equivalent command line interface could be produced with less code and more informative help and error messages by using the argparse
# module:
# 

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--output')
    parser.add_argument('-v', dest='verbose', action='store_true')

    args = parser.parse_args()

    # ... do something with args.output ...
    # ... do something with args.verbose ..
