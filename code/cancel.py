import asyncio
from asyncio import CancelledError


async def long_run():
    print("Starting long_run")
    try:
        await asyncio.sleep(10)
    except CancelledError:
        print("Cancelled long_run")

    print("Finishing long_run")


async def short_run():
    print("Starting short_run")
    await asyncio.sleep(2)
    print("Finishing short_run")


async def run():
    short_task = asyncio.create_task(short_run())
    long_task = asyncio.create_task(long_run())

    await short_task
    long_task.cancel()


asyncio.run(run())
