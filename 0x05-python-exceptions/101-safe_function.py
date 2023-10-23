#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        div_result = fct(*args)
    except ZeroDivisionError as err:
        div_result = None
        print("Exception:", err, file=sys.stderr)
    except IndexError as er:
        div_result = None
        print("Exception:", er, file=sys.stderr)
    return (div_result)
