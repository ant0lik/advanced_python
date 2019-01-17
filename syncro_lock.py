from threading import Lock, Thread
from time import sleep

lock = Lock()
seq = range(101)


def printer(odd):
    for i in seq:
        with lock:
            if i % 2 == odd:
                print(i)
        sleep(0.01)


t1 = Thread(target=printer, args=(False,))
t2 = Thread(target=printer, args=(True,))
t1.start()
t2.start()
