"""This script prints out numbers from 0 to 100 in order."""
from multiprocessing import Process
from multiprocessing import Pipe

even = [i for i in range(101) if i % 2 == 0] + ['end']
odd = [i for i in range(101) if i % 2 != 0] + ['end']


def even_nums(conn):
    """Send even nums, print out odd nums."""
    while even:
        num = even.pop(0)
        conn.send(num)
        received_num = conn.recv()
        if received_num == 'end':
            break
        print(received_num)
    conn.close()


def odd_nums(conn):
    """Send odd nums, print out even nums."""
    while odd:
        num = odd.pop(0)
        received_num = conn.recv()
        if received_num == 'end':
            break
        print(received_num)
        conn.send(num)
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    c = Process(target=even_nums, args=(child_conn,))
    p = Process(target=odd_nums, args=(parent_conn,))
    c.start()
    p.start()
    c.join()
    p.join()
