# Python Optparse
# optparse — Parser for command line options.
# optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module.
# optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command
# line.
# optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you.
# 
# Option.ALWAYS_TYPED_ACTIONS. 
# Actions that always take a type (i.e. whose options always take a value) are additionally listed here.
# The only effect of this is that optparse assigns the default type, "string", to options with no explicit type whose action is listed in
# ALWAYS_TYPED_ACTIONS.
# 
# In order to actually implement your new action, you must override Option’s take_action() method and add a case that recognizes your action.
# 
# For example, let’s add an "extend" action. This is similar to the standard "append" action, but instead of taking a single value from the command-line and
# appending it to an existing list, "extend" will take multiple values in a single comma-delimited string, and extend an existing list with them.
# That is, if --names is an "extend" option of type "string", the command line
# 

# --names=foo,bar --names blah --names ding,dong
 
#
# would result in a list
# 

# ["foo", "bar", "blah", "ding", "dong"]

# 
# Again we define a subclass of Option:
# 

class MyOption(Option):

    ACTIONS = Option.ACTIONS + ("extend",)

    STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
    TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)

    ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

    def take_action(self, action, dest, opt, value, values, parser):

        if action == "extend":
            lvalue = value.split(",")

            values.ensure_value(dest, []).extend(lvalue)

        else:
            Option.take_action(
                self, action, dest, opt, value, values, parser)

#
# Features of note:
#
# > "extend" both expects a value on the command-line and stores that value somewhere, so it goes in both STORE_ACTIONS and TYPED_ACTIONS.
# > to ensure that optparse assigns the default type of "string" to "extend" actions, we put the "extend" action in ALWAYS_TYPED_ACTIONS as well.
# > MyOption.take_action() implements just this one new action, and passes control back to Option.take_action() for the standard optparse actions.
# > values is an instance of the optparse_parser.Values class, which provides the very useful ensure_value() method. ensure_value() is essentially
#   getattr() with a safety valve; it is called as
 
values.ensure_value(attr, value)

