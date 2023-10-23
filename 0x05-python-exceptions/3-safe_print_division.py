#!/usr/bin/python3
def safe_print_division(a, b):
    m = 1
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        m = 0
    finally:
        if m == 1:
            print("Inside result: {:.1f}".format(result))
            return (result)
        else:
            print("Inside result: {:s}".format("None"))
            return (None)
