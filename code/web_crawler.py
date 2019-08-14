import asyncio
import re
from asyncio import TimeoutError
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup

visited_urls = set()


def get_links(html_text):
    anchors = BeautifulSoup(html_text, features="html.parser").find_all('a', attrs={'href': re.compile(r"^/")})
    return [a.get('href') for a in anchors]


async def crawl(url, depth):
    if depth > 1:
        return

    if len(visited_urls) == 100:
        return

    if url in visited_urls:
        print(f"Skipping visited url: {url}")
        return

    if url.endswith(".mp4"):
        return

    visited_urls.add(url)

    # print(f"Crawling {url} at depth {depth}")

    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        try:
            async with session.get(url, allow_redirects=False) as response:
                if response.status == 200:
                    response_text = await response.text()
                    print(f"{url} Length: {len(response_text)}")

                    if 'text/html' in response.headers['Content-Type']:
                        links = get_links(response_text)

                        tasks = []
                        for l in links:
                            url_parts = urlparse(url)
                            next_link = f"{url_parts.scheme}://{url_parts.netloc}{l}"
                            tasks.append(asyncio.create_task(crawl(next_link, depth + 1)))

                        await asyncio.gather(*tasks)
                else:
                    print(f"Failed to get {url}. Status: {response.status}")
        except TimeoutError:
            print(f"Timeout: {url}")


async def run(urls):
    print(urls)
    tasks = []
    for u in urls:
        print(f"Starting crawl for {u}")
        tasks.append(asyncio.create_task(crawl(u, 0)))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(run([
        "https://www.apple.com/",
        "https://en.wikipedia.org/wiki/Portal:Featured_content"
    ]))
