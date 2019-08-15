import asyncio


async def raiser():
    raise Exception("An exception was raised")


async def main():
    raiser_future = asyncio.ensure_future(raiser())
    hello_world_future = asyncio.create_task(asyncio.sleep(1.0, "I have returned!"))

    coros = {raiser_future, hello_world_future}

    finished, pending = await asyncio.wait(coros, return_when=asyncio.ALL_COMPLETED)

    assert raiser_future in finished
    assert raiser_future not in pending
    assert hello_world_future in finished
    assert hello_world_future not in pending

    print(raiser_future.exception())
    print(hello_world_future.result())


asyncio.run(main())
