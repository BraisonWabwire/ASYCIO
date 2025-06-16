import asyncio

# Define a coroutine that simulates a time consuming task
async def fetch_data(delay):
    print("Fetching data ...")
    await asyncio.sleep(delay)
    print("data fetched")
    return {"data":"some data"}

#Another coroutine that calls the first coroutine
async def main():
    print("start on main coroutine")
    task=fetch_data(2)
    result= await task
    print(f'Recieved result:{result}')
    print("End of main coroutine")

asyncio.run(main())