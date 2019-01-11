#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(50000)


def fact(n):
    return 1 if n < 2 else n * fact(n-1)


print(fact(51000))
