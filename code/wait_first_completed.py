import asyncio


async def raiser():
    raise Exception("An exception was raised")


async def main():
    raiser_future = asyncio.ensure_future(raiser())
    hello_world_future = asyncio.create_task(asyncio.sleep(1.0, "I have returned!"))
    coros = {raiser_future, hello_world_future}
    finished, pending = await asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED)

    assert raiser_future in finished
    assert raiser_future not in pending
    assert hello_world_future not in finished
    assert hello_world_future in pending
    print(raiser_future.exception())

    err_was_thrown = None
    try:
        print(hello_world_future.result())
    except asyncio.InvalidStateError as err:
        err_was_thrown = err
    assert err_was_thrown


asyncio.run(main())
