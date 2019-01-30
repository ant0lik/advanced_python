"""This script downloads a number of files using asyncio and threads."""
import aiofiles
import aiohttp
import async_timeout
import asyncio
import os
from time import time as timer

sem = asyncio.Semaphore(3)

links = (
    "https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz",
    "https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz",
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz",
    "https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz",
    "https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz",
    "https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz",
)


async def async_download(session, url):
    """Download asynchronously."""
    async with sem:
        with async_timeout.timeout(86):
            async with session.get(url) as response:
                assert response.status == 200
                filename = os.path.basename(url)
                async with aiofiles.open(filename, 'wb') as f_handle:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        await f_handle.write(chunk)
        return await response.release()


async def main(loop, link):
    """Run main."""
    async with aiohttp.ClientSession(loop=loop) as session:
        await async_download(session, link)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start = timer()

    loop.run_until_complete(
        asyncio.gather(*(main(loop, link) for link in links))
    )
    print("Elapsed time: {}".format(timer() - start))
