import asyncio


async def my_simple_async_fun():
    # await is not used in this function, but it is async function
    print("This is simple async function")
    return "Hi async!"


# main() is defined with async because it is a rule in Python that you can only use the await keyword inside an async function.
async def main():
    # await keyword is required when you call my_simple_async_fun function because my_simple_async_fun definded using async
    result = await my_simple_async_fun()
    print("result:", result)


# When you create a function using async def in Python, it cannot be executed directly like a regular function. To run it, you need a "manager" known as an Event Loop. asyncio.run() is that exact manager.

# asyncio.run() is used to execute a function that is defined with async.
asyncio.run(main())