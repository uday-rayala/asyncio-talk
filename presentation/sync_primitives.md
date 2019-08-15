Source: https://docs.python.org/3/library/asyncio-sync.html

- asyncio synchronization primitives are designed to be similar to those of the threading module with two important caveats:

- asyncio primitives are not thread-safe, therefore they should not be used for OS thread synchronization (use threading for that);
methods of these synchronization primitives do not accept the timeout argument; use the asyncio.wait_for() function to perform operations with timeouts.

asyncio has the following basic synchronization primitives:

- Lock
- Event
- Condition
- Semaphore
- BoundedSemaphore

[Next](./what_next.md)