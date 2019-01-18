"""This script demonstrates synchronization using Semaphore."""
import threading
import time

seq = list(range(101))


def even_nums(ws, rs):
    """Print the next item from the sequence."""
    while seq:
        ws.acquire()
        item = seq.pop(0)
        print(item)
        rs.release()


def odd_nums(ws, rs):
    """Print the next item from the sequence."""
    while True:
        rs.acquire()
        if not seq:
            break
        item = seq.pop(0)
        print(item)
        ws.release()


even_sem = threading.Semaphore(1)
odd_sem = threading.Semaphore(0)

et = threading.Thread(name='even_nums',
                      target=even_nums, args=(even_sem, odd_sem))
ot = threading.Thread(name='odd_nums',
                      target=odd_nums, args=(even_sem, odd_sem))

et.start()
time.sleep(2)
ot.start()
