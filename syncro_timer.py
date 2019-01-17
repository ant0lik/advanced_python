"""This script demonstrates synchronization using Timer."""
from threading import Thread, Timer
from time import sleep

seq = range(101)


def printer(odd):
    """Print even and odd numbers in sequence."""
    for i in seq:
            if i % 2 == odd:
                print(i)
            sleep(0.6)


t1 = Timer(1, printer, [False])
t2 = Timer(1.5, printer, [True])
t1.start()
t2.start()
