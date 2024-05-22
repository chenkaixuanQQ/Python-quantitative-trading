# import time, os
# from multiprocessing import Pool


# def func1( a, b, c = 3, d = 4):
#     print("f1开始运行，子进程ID：{0}，传入参数：{1}".format(os.getpid(), a))
#     print("开始睡眠{0}秒：".format(b))
#     time.sleep(b)
#     a *= 2
#     c *= 2
#     d *= 2
#     print("f1执行结束，子进程ID：{0}，传入参数执行结果：{1}".format(os.getpid(), a))
#     return a,c,d

# def func2(x):
#     print("f2开始运行，子进程ID：{0}，传入参数：{1}".format(os.getpid(), x))
#     time.sleep(3)
#     x *= 2
#     print("f2执行结束，子进程ID：{0}，传入参数执行结果：{1}".format(os.getpid(), x))
#     return x


# if __name__ == "__main__":

#     #定义三个Pool
#     pool_1 = Pool(2)
#     pool_2 = Pool(2)
#     pool_3 = Pool(2)

#     #定义三个可迭代对象
#     x1 = "abcdef"
#     x2 = [1,2,3,4,5,6]
#     x3 = "jklmn"

#     ret = []   #接受返回值
#     t0 = time.time() #计时

#     for i in x2:
#         ret2 = pool_1.apply_async( func = func1, args = ( i, 3 ), kwds = { "c" : 5, "d" : 6})
#         ret.append(ret2)

#     ret3 = pool_2.map_async( func2, x1)
#     ret4 = pool_3.map( func2, x3)

#     while True:
#         if time.time() - t0 >= 5:
#             pool_1.close()
#             pool_2.terminate()
#             pool_3.close()
#             pool_1.join()
#             pool_2.join()
#             pool_3.join()
#             print("pool_1进程返回值：",[ret2.get() for ret2 in ret])
#             print("pool_2进程返回值：",ret3.get())
#             print("pool_3进程返回值：",ret4)
#             break
#         time.sleep(0.5)






# import time, os
# from multiprocessing import Process, Queue 

# def func( a, b, queue, c = 3, d = 4):
#     print("f1开始执行，子进程ID：{0}， 传入参数{1}".format(os.getpid(),a))
#     time.sleep(b)
#     a *= 2
#     c *= 2
#     d *= 2
#     print("f1执行结束，子进程ID：{0}， 传入参数执行结果：{1}".format(os.getpid(), a))
#     queue.put((a,c,d))


# if __name__ == "__main__":
#     queue = Queue()
#     f1 = Process( target = func, args = (10,2,queue), kwargs = {"c" : 5, "d" : 6})
#     f1.start()
#     f1.join()
#     print("子进程的返回值是：", queue.get())
#     queue.close()




# import time
# import threading


# def func( a, b, y, c = 3, d = 4):
#     print("开始执行子线程：",a,"c + d：",c+d)
#     t0 = time.time()
#     global x
#     x = y
#     time.sleep(b)
#     print("子线程" + a + "的x：",x)
#     print("子进程" + a + "执行结束，用时：", time.time() - t0)

# x = 60
# f1 = threading.Thread( target = func, args = ( "f1", 2, 10), kwargs = {"c" : 5, "d" : 6})
# f2 = threading.Thread( target = func, name = "mm", args = ( "f2", 6, 100), kwargs = {"c" : 7, "d" : 8})
# f3 = threading.Thread( target = func, name = "nn", args = ( "f3", 10, 200), kwargs = {"c" : 9, "d" : 10})
# t0 = time.time()
# f1.setName("Kaikai")
# f1.start()

# print("f1执行状态：",f1.is_alive())
# f1.join()
# print("f1执行状态：", f1.is_alive())

# f2.start()
# f3.start()
# print("当前线程变量：",threading.current_thread())
# print("正在执行的线程列表：",threading.enumerate())
# print("正在执行的线程数量：",threading.active_count())
# print("f2执行状态", f2.is_alive())
# f2.join(2)
# print("f2执行状态", f2.is_alive())
# print("子线程f1的名称：{0}，即：{1}".format(f1.name,f1.getName()))
# print("子线程f2的名称：{0}，即：{1}".format(f2.name,f2.getName()))
# print("子线程f3的名称：{0}，即：{1}".format(f3.name,f3.getName()))

# print("主线程的x：",x)
# print("主线程执行结束，用时：", time.time() - t0)








# import time
# import threading
# def consumer( con, n ):
#     global num
#     m = 0
#     t0 = time.time()
#     con.acquire()
#     while True:
#         time.sleep(1)
#         if num <= 0:
#             print( n + "已消费完，等待生产" )
#             m = 0
#             con.notify()
#             if time.time() - t0 >= 5:
#                 break
#             con.wait()
#         else:
#             num -= 1
#             m += 1
#             print( n + "消耗了数量：", m)
#     con.release()


# def producer( con, n ):
#     global num
#     t0 = time.time()
#     con.acquire()
#     while True:
#         time.sleep(1)
#         if num >= 5:
#             print( n + "已生产完，等待消费" )
#             con.notify()
#             if time.time() - t0 >= 5:
#                 break
#             con.wait()
#         else:
#             num += 1
#             print( n + "生产了数量：", num)
#     con.release()

# num = 0
# con = threading.Condition()
# cons = threading.Thread( target = consumer, args = ( con, "c"))
# prod = threading.Thread( target = producer, args = ( con, "p"))
# cons.start()
# prod.start()




# import time,random
# import threading


# def traffic_light(event,light_condition):
#     while light_condition.is_set():
#         event.set()
#         print("现在是绿灯时间，通行3秒后将转为红灯！")
#         time.sleep(3)
#         event.clear()
#         print("现在是红灯时间，禁行5秒后通行！")
#         time.sleep(5)
#     print("红绿灯线程已停止运行")

# def car(event,light_condition):
#     while light_condition.is_set():
#         time.sleep(random.randint(1,2))
#         if event.is_set():
#             print("车辆正常通行！")
#         else:
#             print("红灯时间，车辆等待中！")
#     print("车辆线程已停止运行")

# event = threading.Event()
# light_condition = threading.Event()
# #确保事件启动：
# event.set()
# light_condition.set()

# #创建线程：
# light = threading.Thread( target = traffic_light, args = ( event, light_condition))
# car_pass = threading.Thread( target = car, args = ( event, light_condition ))

# # traffic_light(event,light_condition)

# light.start()
# car_pass.start()


# # print("进程结束！！！！！")
# time.sleep(20)
# light_condition.clear()

# light.join()
# car_pass.join()
# print("所有线程均已结束！")



import time
import threading, queue

def consumer( queue, name ):
    if not queue.empty():
        v = queue.get()
        time.sleep(0.5)
        print( name + "消耗了值：", v)

    else:
        time.sleep(0.5)
        print("消费者无处消费！")

def producer( queue, name, i ):
    for t in i:
        queue.put(t)
        time.sleep(0.5)
        print(name + "生产了值：", t)

#初始化数据：
data1 = [1,2,3]
data2 = [( 1, "abc" ), ( -3, -8 ), ( 5, -9 )]

#初始化队列：
qQue = queue.Queue(3)
qLifo = queue.LifoQueue(3)
qPrio = queue.PriorityQueue(3)

#先进先出：
pQue = threading.Thread( target = producer, args = ( qQue, "先进先出qQue", data1))
pQue.start()
pQue.join()

for i in data1:
    cQue = threading.Thread( target = consumer, args = ( qQue, "先进先出cQue"))
    cQue.start()
    cQue.join()


print("\n\n\n")


#Lifo：
pLifo = threading.Thread( target = producer, args = ( qLifo, "后进先出pLifo", data1))
pLifo.start()
pLifo.join()

for i in data1:
    cLifo = threading.Thread( target = consumer, args = ( qLifo, "后进先出cLifo"))
    cLifo.start()
    cLifo.join()


print("\n\n\n")


#Priority
pPrio = threading.Thread( target = producer, args = ( qPrio, "最小值先出pPrio", data2))
pPrio.start()
pPrio.join()

for i in data2:
    cPrio = threading.Thread( target = consumer, args = ( qPrio, "最小值先出cPrio"))
    cPrio.start()
    cPrio.join()