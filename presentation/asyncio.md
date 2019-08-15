## Coroutines with async/await

- Coroutines are a kind of concurrent programming that works collaboratively. 
- async Coroutines are cooperative unlike python threads which are preemptive.
- Each coroutine is a line of execution that can suspend its control of the program to allow another coroutine to run. 
- This is particularly useful when a coroutine is waiting for something like a network request to complete.


```python
import asyncio


async def main():
    print('hello')
    # Pause here and comeback after sleep 
    await asyncio.sleep(5)
    print('world')

asyncio.run(main())
```
[Code](../code/coroutines.py)

[io_bound]: ./io_bound.png
![alt text][io_bound]

- `async def` will make the function a coroutine.
- Calling `main()` will not execute it but returns a coroutine.
- `await` will suspend current coroutine and resume after the calling coroutine returns.  

## Awaitables
An object is an awaitable object if it can be used in an await expression.

There are three main types of awaitable objects: 
- coroutines
- Tasks
- Futures
- Objects with `__await__()`

## Await Coroutine
```python
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
```
[Code](../code/await_coroutine.py)


## Await Tasks
```python
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(1, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
```
[Code](../code/await_tasks.py)

- Tasks are used to schedule coroutines concurrently.
- When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon.

## Await Futures (Low Level)

- low-level awaitable object that represents an eventual result of an asynchronous operation.
- When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.
- Allow callback-based code to be used with async/await.
- Normally there is no need to create Future objects at the application level code.

## Event Loop (Low Level)
- The event loop keeps track of active tasks, and when one releases control, the event loop will pass control to another.
- The event loop is aware of each task and knows what state it’s in.
- Multiple implementations of event loops. Can be replaced with other custom implementations.


[event_loop]: https://learning.oreilly.com/library/view/asyncio-recipes-a/9781484244012/images/470771_1_En_2_Chapter/470771_1_En_2_Fig1_HTML.jpg
![alt text][event_loop]


## Error Handling
- Any exceptions raised in coroutines are returned to the calling coroutine
- `set_exception_handler()` can used to configure exception handler on an event loop.
[Code](../code/errors.py)

## Cancel Tasks

- Tasks can be cancelled with `.cancel()` method.
- This will raise `CancelledError` exception at await.
- If this exception is not caught, coroutine will be terminated.

[Code](../code/cancel.py)

- `asyncio.shield()` can be used to not cancel.

## Gather 

```
awaitable asyncio.gather(
    *aws, 
    loop=None, 
    return_exceptions=False
)
```
- `asyncio.gather` runs awaitable objects concurrently.
- If all awaitables are completed successfully, the result is an aggregate list of returned values. The order of result values corresponds to the order of awaitables in aws.
- If return_exceptions is False (default), the first raised exception is immediately propagated to the task that awaits on gather(). Other awaitables in the aws sequence won’t be cancelled and will continue to run.
- If return_exceptions is True, exceptions are treated the same as successful results, and aggregated in the result list.

[Code](../code/gather.py)

## Timeouts
```
coroutine asyncio.wait_for(aw, timeout, *, loop=None)
```

- Wait for the `aw` awaitable to complete with a timeout.
- If aw is a coroutine it is automatically scheduled as a Task.
- timeout can either be None or a float or int number of seconds to wait for. If timeout is None, block until the future completes.
- If a timeout occurs, it cancels the task and raises asyncio.TimeoutError.
- To avoid the task cancellation, wrap it in shield().

[Code](../code/timeout.py)

## Waiting
```
coroutine asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
```

- Run awaitable objects in the aws set concurrently and block until the condition specified by return_when.

Usage:
```python
done, pending = await asyncio.wait(aws)
```

return_when indicates when this function should return. It must be one of the following constants:
- FIRST_COMPLETED - The function will return when any future finishes or is cancelled. [Code](../code/wait_first_completed.py)
- FIRST_EXCEPTION - The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED. [Code](../code/wait_first_exception.py)
- ALL_COMPLETED - The function will return when all futures finish or are cancelled. [Code](../code/wait_all_completed.py)


- Unlike wait_for(), wait() does not cancel the futures when a timeout occurs.


## Executor
- Useful when there is no asyncio-compatible library.
- Thread or Process pools can be created to run blocking code.
- asyncio already has a thread pool which we can also use. 

[Code](../code/executor.py)

[Next](./sync_primitives.md)