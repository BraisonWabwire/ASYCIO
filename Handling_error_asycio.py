import asyncio

async def fetch_data(id, sleep_time):
    print(f"coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id":id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Create a list to store the results
    tasks=[]
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([2,1,3], start=1):
            task=tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)
    # After all the task groups have been completed
    results=[task.result() for task in tasks]

    for result in results:
        print(f"Recieved result:{result}" )

asyncio.run(main())
