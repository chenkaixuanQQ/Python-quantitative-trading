# def func(n):
#     m = n
#     print("第", m - n + 1, "次调用_next_()")
#     while n > 0 :
#         print("第", m - n + 1, "次挂起")
#         yield n
#         n -= 1
#         print("第", m - n, "次释放")
#     print("第", m - n + 1,"次调用_next_()")
#
#
# y = func(3)
# for i in y:
#     print("第", 4 - i,"次调用/循环")


# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#     # 使用生成器
# for num in fibonacci(10):
#     print(num)

# dic = {"a" : 1, "b" : 2, "c" : 3}
# for i in dic:
#     print(dic[i])


# def pow(x):
#     return x**2
#
# t = (1,2,3,4,5,6,7)
# It = map(pow,t)
# for i in map(pow,t):
#     print(i)



# def consumer(x,c):
#     print("子生成器" + c + "等待接收任务");
#     r = None;
#     while True:
#         print(c + "准备执行乘：", x)
#         task = yield c + "产生了值" + str(r)
#         if task != None:
#             print(c + "处理任务，结果是", task*x)
#             r = task * x
#             if c == "c1" and task >= 3: break
#             elif c == "c2" and tast >= 6: break
#     return "子生成器" + c + "执行完成，执行了乘" + str(x)
#
#
# def machine(): #Delegate generator
#     print("调用委派生成器")
#     x1 = yield from c1
#     print("c1释放，返回值x1为：", x1)
#     x2 = yield from c2
#     print("c1释放，返回值x2为：", x2)
#
#
#
#
#
# tasks = [1,2,3,4,5,6]
# c1 = consumer(2,"c1")
# c2 = consumer(3,"c2")
# c1.__next__();
# c1.__next__();
# c1.__next__();
# c1.__next__();
# c1.__next__();
# c1.__next__();


# print(type(4))
# print(isinstance("87",object))
# print(isinstance(4,object))
# print(isinstance(2.0,object))
# L = [1,2,3]
# print(isinstance(L,object))
# LM = (1,2,3)
# print(isinstance(LM,object))
#
# lmm = {"a" : 2 , "b" : 3}
# arr = iter(lmm)
# print(isinstance(lmm,object))
# print(isinstance(arr,object))


# class Stu():
#     _leg = 2
#     _mood = "good"
#     def __init__(self,name,StuNum,age = 18):
#         self.name = name
#         print("name: ",name);
#         self.StuNum = StuNum
#         print("Student number: ", StuNum)
#
# m = Stu(name = "Kaikai", StuNum = 202321030146, age = 20)
# print(m.name)
# print(m._mood)



# class Stu():
#     def __init__(self, name, StuNum, EngMarks, MathMarks, ChinMarks):
#         self.name = name
#         self.StuNum = StuNum
#         self.EngMarks = EngMarks
#         self.MathMarks = MathMarks
#         self.ChinMarks = ChinMarks

# class Stu():
#     def __init__(self, name, StuNum, Grade : dict):
#         self.name = name
#         self.StuNum = StuNum
#         self.Grade = Grade
#
#
#     def Print(self):
#         print("The ID of" , self.name , "is", self.StuNum)
#         for i in self.Grade:
#             print(self.name, "got", self.Grade[i], "point in", i)
#
# zhangsan = Stu("zhangsan", "123", {"English marks" : 92.5, "Methematics marks" : 114.5, "Chinese marks" : 91})
#
# zhangsan.Print()


#
# class Stu():
#     def __init__(self, name, Stu_ID):
#         self.name = name
#         self.Stu_ID = Stu_ID
#         self.Grades = {"Mathematics" : 0, "English" : 0, "Chinese" : 0}
#
#     def set_Grade(self, subject : str, marks : float):
#         if subject in self.Grades:
#             self.Grades[subject] = marks
#         else:
#             print(subject, "doesn't exit!!!")
#
#     def Grade_Print(self):
#         print("Name: ", self.name, "   ", "Student ID: ", self.Stu_ID)
#         for course in self.Grades:
#             print(course ,": ", self.Grades[course])
#
# zhangsan = Stu("zhangsan", "10086")
# zhangsan.set_Grade("Mathematics", 132.5)
# zhangsan.set_Grade("English", 122.5)
# zhangsan.set_Grade("Chinese", 99.0)
# zhangsan.Grade_Print()

class Employee():
    def __init__(self, name, Job_Num):
        self.name = name
        self.Job_Num = Job_Num

    def Print_Info(self):
        print(self.name , ": ", self.Job_Num)

class Full_Time(Employee):
    def __init__(self, name : str, Job_Num : str, monthly_salary = 0):
        super().__init__(name,Job_Num)
        self.monthly_salary = monthly_salary

class Part_Time(Employee):
    def __init__(self,name : str, Job_Num : str ,daily_salary = 0, work_days = 0):
        super().__init__(name,Job_Num)
        self.daily_salary = daily_salary
        if work_days <= 31:
            self.work_days = work_days
        self.monthly_salary = daily_salary * work_days

zhangsan = Full_Time("zhangsan", "10086", 3000)
zhangsan.Print_Info()
print(zhangsan.monthly_salary)

lisi = Part_Time("lisi", "12123", 120, 25)
lisi.Print_Info()
print(lisi.monthly_salary)