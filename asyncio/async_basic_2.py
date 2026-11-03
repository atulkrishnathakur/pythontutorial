import asyncio

async def square(number: int) -> int:
    return number * number

# main() is defined with async because it is a rule in Python that you can only use the await keyword inside an async function.
async def main() -> None:

    # await keyword is required when you call square() function because square() definded using async
    x = await square(10)
    print(f'x={x}')

    y = await square(5)
    print(f'y={y}')

    print(f'total={x+y}')


# When you create a function using async def in Python, it cannot be executed directly like a regular function. To run it, you need a "manager" known as an Event Loop. asyncio.run() is that exact manager.

# asyncio.run() is used to execute a function that is defined with async.
asyncio.run(main())