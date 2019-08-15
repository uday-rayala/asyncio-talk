import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

import requests


def get_link(url):
    requests.get(url).status_code


links = ["https://apple.com"] * 100

# start_time = time.time()
# [get_link(i) for i in links]
# duration = time.time() - start_time
# print(f"Sync Duration: {duration} seconds")

start_time = time.time()
with ProcessPoolExecutor() as pool:
    list(pool.map(get_link, links))
duration = time.time() - start_time
print(f"Process pool Duration: {duration} seconds")

start_time = time.time()
with ThreadPoolExecutor() as pool:
    list(pool.map(get_link, links))

duration = time.time() - start_time
print(f"Thread pool Duration: {duration} seconds")
