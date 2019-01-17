"""This script demonstrates synchronization using Event."""
from threading import Event
from threading import Thread
from time import sleep

ev = Event()
even_nums = (i for i in range(101) if i % 2 == 0)
odd_nums = (i for i in range(101) if i % 2 != 0)


def print_even_nums(ev):
    """Print even numbers."""
    for i in even_nums:
        print(i)
        ev.set()
        sleep(0.49)


def print_odd_nums(ev):
    """Print odd numbers."""
    for i in odd_nums:
        while not ev.is_set():
            ev.wait(0.21)
        print(i)
        sleep(0.50)


cs = Thread(target=print_even_nums, args=(ev,))
pd = Thread(target=print_odd_nums, args=(ev,))
pd.start()
sleep(2)
cs.start()
