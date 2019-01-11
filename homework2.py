"""This script causes a segmentation fault."""
import sys


sys.setrecursionlimit(50000)


def foo(n):
    """Create an infinite recursion function."""
    return foo(n - 1)


if __name__ == "__main__":
    foo(1)
