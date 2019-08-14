import asyncio


async def failing_func():
    raise RuntimeError("Failure")


async def success_func():
    print("Success")


async def run():
    await success_func()
    await failing_func()
    await success_func()


asyncio.run(run())
