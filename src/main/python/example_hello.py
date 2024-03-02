"""
This is a simple module to demonstrate a hello world function in Python.
"""

import sys

def hello_world(out):
    """
    Prints \"Hello World!\".
    >>> import sys
    >>> hello_world(sys.stdout)
    Hello World!\n
    """
    out.write("Hello world of Python\n")


if __name__ == "__main__": # pragma: no cover
    import doctest
    doctest.testmod()

