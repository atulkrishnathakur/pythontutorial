
import asyncio

async def my_simple_async_function():
    # await is not used in this function, but it is async function
    print("This is simple async function")
    return "Hi async!"


# When you create a function using async def in Python, it cannot be executed directly like a regular function. To run it, you need a "manager" known as an Event Loop. asyncio.run() is that exact manager.

# asyncio.run() is used to execute a function that is defined with async.
    
result = asyncio.run(my_simple_async_function())

print(result)