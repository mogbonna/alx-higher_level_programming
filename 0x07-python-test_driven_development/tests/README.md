==================================================
# Doc for explain how use TestsCases on TDD Project
===================================================

Let's start with the way a test has:
0. Integers addition module:
====================

## Import module:
    >>> add_integer = __import__('0-add_integer').add_integer
### Comment: Mandatory import (file_name).func_name

## Function:
=======.
Write a function that adds 2 integers.

Operations:
=========
a and b must be integers or floats, otherwise raise a TypeError exception
with the message a must be an integer or b must be an integer:

### A test example of 0-add_integer.txt:

a must be integers or float (Comment: name of test case)
    >>> add_integer(None, 3) (Comment: line that the program exec)
    Traceback (most recent call last):
    TypeError: a must be an integer (Comment: corresponding error)


b must be integers or float
    >>> add_integer(3, None)
    Traceback (most recent call last):
    TypeError: b must be an integer


### How does it work?
We have a sum function, def sum(a, b = 89) the sum has 89 assigned in var b. Let's run the test.

run : python3 -m doctest ./tests/0-add_integer.txt
The success would be: nothing to show


The failed would be message: ***Test Failed*** <number of tests> failures.



## Types of tests (examples)

### TYPES

Many cases of vars types.

    >>> function1(3.0, 5) (Comment: float, int)
    8

    >>> function1(-4.4, -5) (Comments: negative float, negative int)
    -9.4

Many cases of type return with int

    >>> type(function1(5, 5))
    <class 'int'>

### ARGS

When we must be careful of the arguments, for example: if the arguments are required in the parameters of a function.

    >>> function1() (Comment: without parametrs)
    Traceback (most recent call last):
    TypeError: add_integer() missing 1 required positional argument: 'a'

When the required arguments have no assigned value.

    >>> function1(a, 123) (Comment: args empty)
    Traceback (most recent call last):
    NameError: name 'a' is not defined


### I/O INPUTS

When we must be careful of data entries, for example: avoiding overflow in functions.

    >>> function1(5, 1e400) (Comment: max integer)
    Traceback (most recent call last):
    OverflowError

Infinity entries.

    >>> function1(999e9999, 1) (Comment: type i floats)
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer

### I/O OUTPUT

    >>> function1(3.0, 5) (Comment: the output should return (same types))
    8


### ERRORS

Error should print
In python not catch errors from anothers. Classification not necessary

    Traceback (most recent call last):
    ...
    TypeError: mssg
    NameError: mssg
    ValueError: mssg
    OverFlowError: mssg

