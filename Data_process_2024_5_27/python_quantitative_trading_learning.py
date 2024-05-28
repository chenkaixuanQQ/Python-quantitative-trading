# import time
# import asyncio

# async def say_after( delay, what ):
#     await asyncio.sleep( delay )
#     print( what )
#     return what

# async def main():
#     print(f"started at {time.strftime("%X")}")
#     # r1 = say_after( 1, "Hello")
#     # r2 = say_after( 2, "world")
#     # print("返回值为：", (r1,r2))


#     #创建任务：
#     task1 = asyncio.create_task( say_after( 3, "Hello" ) )
#     task2 = asyncio.create_task( say_after( 7, "World" ) )

#     #执行任务并等待完成：
#     result = await asyncio.gather( task1, task2 )

#     print( result )


#     print(f"finished at {time.strftime("%X")}")

# asyncio.run(main())









# import time
# import asyncio

# async def say_after( delay, what ):
#     await asyncio.sleep( delay )
#     print(what)
#     return what

# async def main():
#     print(f"started at {time.strftime("%X")}")
#     task1 = asyncio.create_task(say_after( 1, "Hello" ))
#     task2 = asyncio.create_task(say_after( 2, "world" ))
#     # tasks = [task1,task2]

#     # done, pending = await asyncio.wait( [task1,task2],timeout = 1.5 )
#     done, pending = await asyncio.wait( [task1, task2], timeout = 1.5 )

#     print("返回值为：", [r.result() for r in done], pending)

#     print(f"finished at time {time.strftime("%X")}")

# asyncio.run(main())








# import asyncio
# import random
# import time

# #定义工作协程：
# async def worker( name, queue ):
#     while True:
#         print(f"{name}队列当前的元素数量：{queue.qsize()}")
#         sleep_for = await queue.get()

#         #暂停sleep_for秒：
#         print(f"暂停{sleep_for}秒.......")
#         await asyncio.sleep(sleep_for)

#         #通知队列元素已经被处理完成
#         queue.task_done()
#         print(f"{name}等待了 {sleep_for: .2f} 秒")

# #定义主函数协程：
# async def main():
#     #创建先进先出队列：
#     queue = asyncio.Queue()

#     #添加三个随机时间到队列：
#     total_sleep_time = 0

#     for _ in range(3):
#         sleep_for = random.uniform( 0.05, 1.0 )
#         total_sleep_time += sleep_for
#         queue.put_nowait(sleep_for)

#         tasks = []
#         for i in range(2):
#             task = asyncio.create_task( worker(f"worker-{i}", queue))
#             tasks.append(task)
#         started_at = time.monotonic()
#         print(f"队列是否满：{queue.full()}")

#         await queue.join()
#         total_slept_for = time.monotonic() - started_at
#         print(f"队列是否为空：{queue.empty()}")
#         for task in tasks:
#             task.cancel()

#         await asyncio.gather( *tasks, return_exceptions = True )
#         print("====")
#         print(f"任务并发执行时间 {total_slept_for:.2f} 秒")
#         print(f"任务等待时间之和 {total_sleep_time:.2f} 秒")

# asyncio.run( main() )





from datetime import date
from tqsdk import TqApi, TqKq, TqSim, TqBacktest, TqReplay, TqAccount, TqAuth

#使用实盘账号直连行情何交易服务器：
# api = TqApi(TqAccount("H期货公司", "账号", "密码"), auth = TqAuth("信易账户","账户密码"))

#使用simnow模拟账号直连行情何交易服务器
# api = TqApi(TqAccount("simnow", "账号", "密码"), auth = TqAuth("信易账户","账户密码"))

# 使用快期模拟账号连接行情服务器，根据填写的信易账户参数连接指定的快期模拟账户：
# api = TqApi(TqApi(), auth = TqAuth("信易账户","账户密码"))

#使用快期模拟账号连接行情服务器
# api = TqApi(TqKq(), auth = ( "信易账户", "账户密码" ))