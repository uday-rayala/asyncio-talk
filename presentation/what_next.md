[Web Crawler Example](../code/web_crawler.py)

## Things not covered

- asyncio for web servers

## Summary

- Use asyncio for IO workloads and a single ThreadPoolExecutor is not enough.
- Look for asyncio compatible libraries. If not found, use executors for blocking code.
- Debugging might be tricky since the execution flow is not linear. (true for any concurrent program)
- But asyncio programs are simpler to write and easy to reason about.


## References

https://realpython.com/python-concurrency/

https://docs.python.org/3/library/asyncio.html

https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b

https://realpython.com/async-io-python/
 