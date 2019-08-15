import asyncio


async def raiser():
    raise Exception("An exception was raised")


async def main():
    raiser_task = asyncio.create_task(raiser())
    hello_world_task = asyncio.create_task(asyncio.sleep(1.0, "I have returned!"))
    coros = {raiser_task, hello_world_task}

    finished, pending = await asyncio.wait(coros, return_when=asyncio.FIRST_EXCEPTION)

    assert raiser_task in finished
    assert hello_world_task in pending

    print(raiser_task.exception())

    err_was_thrown = None
    try:
        print(hello_world_task.result())
    except asyncio.InvalidStateError as err:
        err_was_thrown = err
    assert err_was_thrown


asyncio.run(main())
