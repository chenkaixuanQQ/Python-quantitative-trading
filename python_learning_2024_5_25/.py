import time
import asyncio

async def say_after( delay, what ):
    time.sleep(delay)
    print(what)
    return what

async def main():
    print(f"started at {time.strftime("%X")}")
    r1 = await say_after(1, "hello")
    print("hakhj")
    r2 = await say_after(2,"world")
    print("返回值为：",(r1,r2))
    print(f"finished at {time.strftime("%X")}")

asyncio.run(main())
print("ahhhhh")





