#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as err:
        print("Exception:", err, file=sys.stderr)
        return (False)
    except TypeError as erro:
        print("Exception:", erro, file=sys.stderr)
        return (False)
