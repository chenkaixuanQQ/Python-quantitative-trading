# print("Hello,python")
# class A():
#     x = 3
#     def __init__(self):
#         self.y = 4
#     @property
#     def test_z(self):
#         z = "abc"
#         return z
    

# test = A()
# print(test.x,test.y,test.test_z)
# try :
#     print(test.test_z())
# except TypeError:
#     print("语法错误")



# import datetime

# print(datetime.datetime .now())
# print(datetime.time(18,58))
# print(__name__)



# a = [1,2,3,4,5,6,7]
# b = a
# b[0] = 100
# print(a is b)


# a = 10
# b = 10
# b = 100
# print(id(a))
# print(id(b))
# print(a is b)
# print(a,b)


# dic = {"a" : 1, "b" : 2}
# cpy = dic
# dic["m"] = 0
# print(dic["m"])
# print(cpy["m"])
# dic = 0
# dic = dict({"a" : 1, "b" : 2})
# print(dic)

# f = open(r"D:\Computer_learning\Python\Python-quantitative-trading\Python_learning_2024_5_19\text.txt",mode = "r+",encoding = "utf-8")
# # f.seek(27)
# f.write("And my mood is very good!!!\n")
# f.write("And my mood is very good!!!\n")
# f.write("And my mood is very good!!!\n")
# f.write("And my mood is very good!!!\n")
# f.flush()
# f.seek(0)
# # data = f.read()
# # for line in f:
# #     print(line)
# line = f.readlines()
# print(line)
# f.close()

# f = open(r"D:\Computer_learning\Python\Python-quantitative-trading\Python_learning_2024_5_19\text.txt",mode = "w+",encoding = "utf-8")
# data = f.read()
# print(data)

# f.write("Hello world")
# f.flush()
# print(data)
# f.close()



import os
from pathlib import Path
p = Path(os.getcwd() + r"\logs")
p.mkdir(exist_ok = True)
