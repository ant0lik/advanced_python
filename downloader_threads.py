"""This script downloads files using threads."""
import os
from queue import Queue
from threading import Thread
from time import time
from urllib.request import urlopen


links = (
    "https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz",
    "https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz",
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz",
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz",
    "https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz",
    "https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz",
)


def download_link(link):
    """Download a file located at the link."""
    download_path = os.path.basename(link)
    with urlopen(link) as _file, open(download_path, 'wb') as f:
        f.write(_file.read())


class DownloadWorker(Thread):
    """Class representing a thread."""

    def __init__(self, queue):
        """Initialize a thread."""
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        """Get a link from the queue and try downloading the file."""
        while True:
            link = self.queue.get()
            try:
                download_link(link)
            finally:
                self.queue.task_done()


def main():
    """Initialize a timer, a Queue, and threads."""
    ts = time()
    queue = Queue()
    for i in range(len(links)):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for link in links:
        queue.put(link)
    queue.join()
    print(f"Elapsed time: {time() - ts}")


if __name__ == "__main__":
    main()
