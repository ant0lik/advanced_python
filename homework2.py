""" Script that causes a segfault. """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(50000)


def fact(n):
    """ Create a recursive factorial command. """

    return 1 if n < 2 else n * fact(n-1)


fact(51000)
