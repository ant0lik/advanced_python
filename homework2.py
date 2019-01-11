"""This script raises a segmentation fault."""
import sys


sys.setrecursionlimit(30000)


def foo(n):
    """Create an infinite recursion."""
    return foo(n - 1)


if __name__ == "__main__":
    foo(1)
