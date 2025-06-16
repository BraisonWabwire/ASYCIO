import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    future.set_result(value)
    print(f"set the future's result to {value}")

async def main():
    # Create a future object
    loop=asyncio.get_running_loop()
    future=loop.create_future()

    asyncio.create_task(set_future_result(future,"future result is ready"))

    result=await future
    print(f"Recieved the future's result:{result}")

asyncio.run(main())