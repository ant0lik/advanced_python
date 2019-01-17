"""This script demonstrates synchronization using Condition."""
from threading import Thread, Condition
from time import sleep

cd = Condition()
even_nums = (i for i in range(101) if i % 2 == 0)
odd_nums = (i for i in range(101) if i % 2 != 0)


def print_even_nums(cd):
    """Print even numbers."""
    for i in even_nums:
        with cd:
            print(i)
            cd.notifyAll()
        sleep(1)


def print_odd_nums(cd):
    """Print odd numbers."""
    for i in odd_nums:
        with cd:
            cd.wait()
            print(i)


pd = Thread(target=print_even_nums, args=(cd,))
cs = Thread(target=print_odd_nums, args=(cd,))
cs.start()
sleep(2)
pd.start()
sleep(2)
