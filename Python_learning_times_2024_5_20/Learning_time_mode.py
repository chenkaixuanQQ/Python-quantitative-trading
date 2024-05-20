# import time
# time.sleep(3)
# print(time.time())
# print(time.process_time_ns())
# print(time.altzone)
# print(time.localtime())
# print(time.gmtime())
# print(time.ctime())
# print(time.asctime())
# print(time.strptime(time.asctime()))
# Time = time.strptime(time.asctime())
# print(time.mktime(Time))
# print(time.time())
# print(time.process_time())



# import time
# from datetime import date
# print(date.max)
# print(date.min)
# print(date.resolution)
# print(date.today())
# print(time.time())
# print(date.fromtimestamp(time.time()))
# print(time.gmtime())


# from datetime import time
# print(time(8,45))
# day_start = time(8,45)
# day_end = time(15,15)
# # print(day_start - day_end)



# import time
# import datetime
# # print(datetime.date.today())
# # print(datetime.datetime.today())
# # print(datetime.utcfromtimestamp(time.time()))


# from datetime import datetime,timedelta

# dt = datetime.today()
# print(dt)
# print(dt + timedelta(1))
# print(dt + timedelta(hours = 1))
# print(dt + timedelta(days = 1, hours = 1))
# print(type(dt))


import time,os
from multiprocessing import Process
def func(a : str, b, y, c = 3, d = 4):
    print("开始执行子进程：", a)
    # time.sleep(1)
    print("子进程" + a + "的ID：{0}, 父进程的ID：{1}".format(os.getpid(),os.getppid()))
    global x
    x = y
    t0 = time.time()
    print("c + d: ", c + d)
    # time.sleep(1)
    print("子进程" + a + "的x：", x)
    time.sleep(b)
    print("子进程" + a + "执行结束，用时：", time.time() - t0)


if __name__ == "__main__":
    x = 60
    f1 = Process(target = func, args = ("f1",3,10), kwargs = {"c" : 5, "d" : 6})
    f2 = Process(target = func, name = "mm", args = ("f2",5,100), kwargs = {"c" : 7, "d" : 8})
    f3 = Process(target = func, name = "nn", args = ("f2",10,200), kwargs = {"c" : 9, "d" : 10},daemon = True)
    t0 = time.time()
    f1.start()
    print("f1执行状态：", f1.is_alive())
    f1.join()
    # time.sleep(10)
    print("f1执行状态：",f1.is_alive())
    f2.start()
    f3.start()
    print("f2执行状态：", f2.is_alive())
    f2.join(2)
    f2.terminate()
    f2.join()
    # time.sleep(10)
    print("f2执行状态：",f2.is_alive())
    print("子进程f1的名称：{0}, pid: {1}".format(f1.name,f1.pid))
    print("子进程f2的名称：{0}, pid: {1}".format(f2.name,f2.pid))
    print("子进程f3的名称：{0}, pid: {1}".format(f3.name,f3.pid))
    print("父进程的x：", x)
    print("父进程执行结束，用时：", time.time() - t0)



