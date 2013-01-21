"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> neith.lib.util.log("test_token")
test_token
"""
import sys
import os

neith_module = os.path.realpath(os.path.abspath("./../.."))
sys.path.append( neith_module )

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)