import sys

"""Prints \"Hello World!\" to the given output stream."""
def hello_world(out):
    """
    Prints \"Hello World!\".
    >>> import sys
    >>> hello_world(sys.stdout)
    Hello World!\n
    """
    out.write("Hello World!\n")


if __name__ == "__main__": # pragma: no cover
    import doctest
    doctest.testmod()
