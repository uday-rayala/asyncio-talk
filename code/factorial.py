import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor


def factorial(n):
    f = 1
    for i in range(1, n):
        f = f * i

    return f


numbers = [10000] * 300

start_time = time.time()
[factorial(i) for i in numbers]
duration = time.time() - start_time
print(f"Sync Duration: {duration} seconds")

start_time = time.time()
with ProcessPoolExecutor() as pool:
    list(pool.map(factorial, numbers))
duration = time.time() - start_time
print(f"Process pool Duration: {duration} seconds")

start_time = time.time()
with ThreadPoolExecutor() as pool:
    list(pool.map(factorial, numbers))

duration = time.time() - start_time
print(f"Thread pool Duration: {duration} seconds")
