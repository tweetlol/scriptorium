import asyncio

async def yo(time): 
    print("HELLLO THERE, fetching data...")
    await asyncio.sleep(time) 
    print(f"data received in {time} seconds, GENERAL KENOBI")


async def main(): # ASYNC => COROUTINE
    print("start of main coroutine")

# asyncio.sleep IS AWAITABLE, time.sleep IS NOT
# AWAIT SPECIFIES WHEN IT'S SAFE TO HAND OVER THE CONTOROL

    task = await yo(2)

    print("data = " + f"{task}")
    print("end of main coroutine")


asyncio.run(main())