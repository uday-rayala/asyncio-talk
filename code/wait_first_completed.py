import asyncio


async def raiser():
    raise Exception("An exception was raised")


async def main():
    # raiser_future = asyncio.ensure_future(raiser())
    fast_task = asyncio.create_task(asyncio.sleep(1.0, "Fast returned!"))
    slow_task = asyncio.create_task(asyncio.sleep(2.0, "Slow returned!"))
    coros = {fast_task, slow_task}

    finished, pending = await asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED)

    assert fast_task in finished
    assert slow_task in pending

    print(fast_task.result())

    err_was_thrown = None
    try:
        print(slow_task.result())
    except asyncio.InvalidStateError as err:
        err_was_thrown = err
    assert err_was_thrown


asyncio.run(main())
