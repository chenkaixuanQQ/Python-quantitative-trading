# import time,os
# from multiprocessing import Process

# def func(a : str, b : int, y : int, c = 3, d = 4):
#     print("开始执行子进程：", a)
#     time.sleep(b)
#     print("子进程" + a + "的ID：{0}     父进程的ID: {1}".format(os.getpid(),os.getppid()))
#     time.sleep(b)
#     global x
#     x = y
#     t0 = time.time()
#     print("c + d: ", c + d)
#     time.sleep(b)
#     print("子进程" + a + "的x：", x)
#     time.sleep(b)
#     print("子进程" + a + "执行结束，用时：", time.time() - t0)


# #多进程任务的一个包装，用来执行多进程任务的一个套
# class MyProcess(Process):
#     def __init__( self, target, args, kwargs ):
#         super().__init__()
#         self.target = target
#         self.args = args
#         self.kwargs = kwargs
#     def run(self):
#         self.target( *self.args, **self.kwargs)


# if __name__ == "__main__":
#     x = 60
#     f1 = MyProcess(target = func, args = ( "f1", 2, 10), kwargs = { "c" : 5, "d" : 6})
#     f2 = MyProcess(target = func, args = ( "f2", 6, 100), kwargs = { "c" : 7, "d" : 8})

#     t0 = time.time()
#     f1.start()
#     print("f1执行状态：", f1.is_alive())
#     # f1.join()
#     # time.sleep(10)

#     print("f1执行状态：", f1.is_alive())

#     f2.start()
#     print("f2执行状态：", f2.is_alive())
#     # f2.join(2)
#     # f2.terminate()
#     # f2.join()
#     # time.sleep(10)

#     print("f2执行状态：", f2.is_alive())
#     print("子进程f1的名称：{0}, pid: {1}".format(f1.name,f1.pid))
#     print("子进程f2的名称：{0}, pid: {1}".format(f2.name,f2.pid))
#     print("父进程的x：", x)
#     print("父进程执行结束，用时：", time.time() - t0)


# import time,os
# from multiprocessing import Process, Lock

# def func(a,b,y,lock,c = 3, d = 4):
#     lock.acquire()
#     print("开始执行子进程：", a)
#     print("子进程" + a + "的ID: {0}     父进程的ID: {1}".format(os.getpid(),os.getppid()))
#     global x
#     x = y
#     t0 = time.time()
#     print("c + d: ", c + d)
#     print("子进程" + a + "的x：", x)
#     time.sleep(b)
#     print("子进程" + a + "执行结束，用时：", time.time() - t0)
#     lock.release()


# if __name__ == "__main__":
#     lock = Lock()
#     x = 60
#     t0 = time.time()
#     for i in range(1,3):
#         for j in "abc":
#             f = Process(target = func, name = i*j, args = ( i*j, i, 10, lock), kwargs = {'c' : 5, 'd' : 6})
#             f.start()
#             print("子进程f的名称：{0},pid: {1}".format(f.name,f.pid))
#             # f.join()
#     print("父进程的x：", x)
#     print("父进程执行结束，用时：", time.time() - t0)




# import time,random
# from multiprocessing import Process, Event


# #用于表示红绿灯交替的函数
# def light( event, stop_event ):
#     while stop_event.is_set():
#         if event.is_set():
#             print("是绿灯，放行，3秒后转为红灯")
#             time.sleep(3)
#             event.clear()
#         else:
#             print("是红灯，禁行，6秒后转为绿灯")
#             time.sleep(6)
#             event.set()

# #用于表示车辆通行情况
# def car( event, number ):
#     event.wait()
#     print("是绿灯，车牌号 {0} 放行！".format(number))


# if __name__ == "__main__":
#     event = Event()  #将Event实例化，用于表示进程的执行状况，即红绿灯状态
#     stop_event = Event()
#     stop_event.set()

#     #开始红绿灯交替工作
#     traffic_light = Process(target = light, args = (event, stop_event))
#     traffic_light.start()

#     for i in "abcde":
#         time.sleep(random.randint(1,2))
#         c = Process( target = car, args = ( event, i ))
#         c.start()


#     #让程序运行20秒后终止程序
#     print("1111111111111111111111111111111111111111111111111111111")
#     # time.sleep(20)  
#     stop_event.clear()

#     traffic_light.join()
#     for c in Process.active_children():
#         c.join()





# from multiprocessing import Queue

# queue = Queue(3)
# queue.put(1)
# queue.put(2)
# queue.put(3)
# print(queue.get())
# print(queue.get())
# print(queue.get())
# print(queue.empty())
# queue.put(4,timeout = 2)



# import time
# from multiprocessing import Process, Queue

# def consumer( queue, n ):
#     for i in range(3):
#         time.sleep(1)
#         v = queue.get()
#         print(n + "消耗了值：", v)

# def producer( queue, n ):
#     for i in range(6):
#         time.sleep(0.6)
#         queue.put(i)
#         print(n + "生产了值：", i)



# if __name__ == "__main__":
#     queue = Queue(2)
#     c1 = Process( target = consumer, args = (queue, "c1"))
#     c2 = Process( target = consumer, args = (queue, "c2"))
#     p = Process(target = producer, args = (queue,'p'))
#     c1.start()
#     c2.start()
#     p.start()



# import os
# from multiprocessing import Process,Pipe

# def func( conn, sendf ):
#     for i in sendf:
#         conn.send(i)
#         print("子进程{0}发送了数据{1}".format(os.getpid(),i))
#     while conn.poll(5):
#         rc = conn.recv()
#         print("子进程{0}接收了数据{1}".format(os.getpid(),rc))


# if __name__ == "__main__":
#     conn1,conn2 = Pipe()

#     sendf1 = "abcde"
#     sendf2 = [1,2,3,4,5]

#     f1 = Process( target = func, args = ( conn1, sendf1 ))
#     f2 = Process( target = func, args = ( conn2, sendf2 ))
    
#     f1.start()
#     f2.start()
#     f1.join()
#     f2.join()
#     conn1.close()
#     conn2.close()




import os  
from multiprocessing import Process, Pipe  
  
def func(conn, send_data):  
    for data in send_data:  
        conn.send(data)  
        print("子进程{0}发送了数据{1}".format(os.getpid(), data))  


    # 注意：这里没有从 conn 接收数据的循环，因为在这个例子中我们不发送任何数据回主进程  
    # 如果需要双向通信，你需要在另一个进程中调用 conn.send()  
  
    conn.close()  # 关闭连接以释放资源  
  
if __name__ == "__main__":  
    # 创建两个管道  
    parent_conn1, child_conn1 = Pipe()  
    parent_conn2, child_conn2 = Pipe()  
  
    sendf1 = "abcde"  
    sendf2 = [1, 2, 3, 4, 5]  
  
    # 传递 child_connX 作为连接对象，send_data 作为要发送的数据  
    f1 = Process(target=func, args=(child_conn1, sendf1))  
    f2 = Process(target=func, args=(child_conn2, sendf2))  
  
    f1.start()  
    f2.start()  
  
    # 你可以从父连接接收数据，但在这个例子中我们没有发送任何数据回主进程  
    # 例如：  
    # for i in range(len(sendf1)):  
    #     print("主进程接收了数据：", parent_conn1.recv())  
    # for i in range(len(sendf2)):  
    #     print("主进程接收了数据：", parent_conn2.recv())  
  
    f1.join()  
    f2.join()  
  
    # 主进程不需要关闭父连接，因为当子进程关闭它们的连接时，父连接也会自动关闭  
    # 但如果你想要明确地关闭它们，可以这样做：  
    # parent_conn1.close()  
    # parent_conn2.close()  
    # 注意：child_connX 在子进程中已经关闭，所以主进程中不需要（也不能）关闭它们







