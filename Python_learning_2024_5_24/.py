# ret = map(lambda x: x ** 2,[1,2,3,4,5,6,7,8] )
# ret = list(ret)
# print(ret)




# import time
# from concurrent.futures import ThreadPoolExecutor

# def func1( a, b, c = 3, d = 4):
#     print("开始执行子线程: ", a, "c + d: ", c + d)
#     t0 = time.time()
#     print(a + "开始睡眠：{0}秒".format(b))
#     time.sleep(b)
#     print("子线程" + str(a) + "执行结束，用时：", time.time() - t0)
#     return a, c, d

# def func2(x):
#     print("开始执行子线程：",x)
#     t0 = time.time()
#     print(x,"睡眠3秒")
#     print("子线程" + str(x) + "执行结束，用时：" ,time.time() - t0)
#     return x

# #回调函数，收集返回值：
# def fn(future):
#     global r2
#     r2.append(future.result())


# pool1 = ThreadPoolExecutor(max_workers = 2)
# pool3 = ThreadPoolExecutor(2)

# x = "abcdef"
# y = [1,2,3,4,5,6]
# z = "jklmn"

# r1 = []  #用于收集future对象
# r2 = []   #用于收集future对象的返回值
# t0 = time.time()

# for i in y:
#     ret = pool1.submit( func1, i, 3, c = 5, d = 6 )  #把线程交给进程池
#     r1.append(ret)         #收集future对象
# pool1.shutdown( wait = False )     #关闭线程池


# #省去了关闭线程池的环节
# with ThreadPoolExecutor(2) as pool2:
#     for i in x:
#         ret = pool2.submit( func1, i, 3, c = 5, d = 6 )
#         ret.add_done_callback(fn)



# r3 = pool3.map( func2, z )
# pool3.shutdown( wait = False )


# print([f.result for f in r1])
# print(r2)
# print(list(r3))
# print("主程序执行结束，用时：", time.time() - t0)




#当前版本不支持使用这个装饰器
# import time
# import asyncio


# #等价于 child = asyncio.coroutine(child)
# @asyncio.coroutine
# def child( t, task ):
#     print(f"start_child time {time.strftime("%X")}", task)
#     # print("start_child time {0}".format(time.strftime("%X")), task)
#     yield from asyncio.sleep(t)
#     print(f"end_child time {time.strftime("%X")}", task)



# @asyncio.coroutine
# def task1( number ):
#     print(f"start_task1 time {time.strftime("%X")}")
#     f = 0
#     for i in range( number ):
#         f += print("task1 + %d" % i)
#         yield from child( 1, task1.__name__)
#         print("task1 the end number = %d" % f)
#         print(f"end_task1 time {time.strftime("%X")}")


# @asyncio.coroutine
# def task2( number ):
#     print(f"start_task2 {time.strftime("%X")}")
#     f = 0
#     for i in range( number ):
#         f *= i
#         print("task2 * %d" % i)
#         yield from child( 1, task2.__name__)

#     print("task2 the end number = %d" % f)
#     print(f"end_task2 time {time.strftime("%X")}")


# print(f"start_main time {time.strftime("%X")}")

# #创建一个事件循环
# loop = asyncio.get_event_loop()

# task_1 = loop.create_task(task1(2))
# loop.run_until_complete(task_1)





# def Loop(i):
#     print("进入")
#     yield i
#     print("挂起")
# M = range(10)
# for c in Loop(M):
#     print(c)





# import time
# import asyncio

# async def main():
#     print(f"started at {time.strftime("%X")}")
#     print("Hello ...")
#     await asyncio.sleep(1)
#     print("... World!")
#     print(f"finished at {time.strftime("%X")}")

# # main()
# asyncio.run(main())





import time
import asyncio

async def stop_loop(delay, loop):
    t0 = time.time()
    print(f"初始时间：{time.strftime("%X")}")
    while True:
        await asyncio.sleep(delay)
        print(f"已等待时间： {time.time() - t0}")
        if time.time() - t0 >= 5:
            t0 = time.time()
            loop.stop()
            print(f"事件停止时间：{time.strftime("%X")}")
            print(f"事件循环是否被关闭：{loop.is_closed()}")
        


loop = asyncio.get_event_loop()
loop.create_task(stop_loop(1,loop))

def wait_update():
    loop.run_forever()

while True:
    time.sleep(1)
    wait_update()
    print("再次开启")