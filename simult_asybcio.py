import asyncio

async def fetch_data(id,sleep_time):
    print(f"coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id":id,"data":f"Sample data from coroutine {id}"}

async def main():
    # Creating simultaneous coroutines using the create_task function

    # task1=asyncio.create_task(fetch_data(1,2))
    # task2=asyncio.create_task(fetch_data(2,3))
    # task3=asyncio.create_task(fetch_data(3,1))
    
    # result1=await task1
    # result2=await task2
    # result3=await task3

    # print(result1,result2,result3)

    # Using the gather function to run multiple coroutine simulaneously
    results=await asyncio.gather(fetch_data(1,2),fetch_data(2,1),fetch_data(3,3))

    for result in results:
        print(f"Recieved Results:{result}")

asyncio.run(main())