import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)

        if number == 100:
            raise RuntimeError("Too big number")

        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Sequential
    # await factorial("A", 2)
    # await factorial("B", 3)
    # await factorial("C", 4)

    # Schedule three calls *concurrently*:
    x = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
        factorial("D", 100),
        return_exceptions=True
    )

    print(x)


asyncio.run(main())
