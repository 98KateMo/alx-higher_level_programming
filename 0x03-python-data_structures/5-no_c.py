#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Delete all characters c and C from the string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))