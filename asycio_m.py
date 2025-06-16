import asyncio

# Define a coroutine that simulates a time consuming task
async def fetch_data(delay, id):
    print("Fetching data ...id:", id)
    await asyncio.sleep(delay)
    print("data fetched....id:",id)
    return {"data":"some data","id":id}

#Another coroutine that calls the first coroutine
async def main():
    task1=fetch_data(2,1)
    task2=fetch_data(2,2)

    result1=await task1
    print(f"recieved result: {result1}")
    result2=await task2
    print(f"Recieed results:{result2}")
   
   
# Run the main coroutine
asyncio.run(main())