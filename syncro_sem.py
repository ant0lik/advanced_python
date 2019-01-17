"""This script demonstrates synchronization using Semaphore."""
from threading import Semaphore, Thread
from time import sleep

sem = Semaphore(1)
seq = range(101)


def printer(odd):
    """Print even and odd numbers in sequence."""
    for i in seq:
        with sem:
            if i % 2 == odd:
                print(i)
        sleep(0.01)


t1 = Thread(target=printer, args=(False,))
t2 = Thread(target=printer, args=(True,))
t1.start()
t2.start()
