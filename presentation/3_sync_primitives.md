## Synchronisation Primitives

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

## Subprocesses

Source: https://docs.python.org/3/library/asyncio-subprocess.html

## Queues to distribute tasks

Source: https://docs.python.org/3/library/asyncio-queue.html

[Next](4_what_next.md)