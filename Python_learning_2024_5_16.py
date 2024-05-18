# import re
# s = "asd134245";
# # ret = re.findall('\\d',s);
# print(ret);
#
# m = (1,4,2,5,7,3);
# #m = sort(m);#Just can sort list!!!
# print(m);
#
#
#
# Tump = ('a','b');
# for i in range(10):
#     Tump = Tump + (i,i+1);
#     print(Tump);
#
# Len = len(Tump);
# print(Tump[99:100]);
#
#
#
#
# dic = { 'a' : 1, 'b' : 2, 'c' : 3};
# for key in dic.keys():
#     print(dic[key], end = ' ');
#
# It = iter(dic);
# print(It);
#
# for key in dic.keys():
#     print(key);
#
# for key in dic.items():
#     print(key);
#
# arr = (1,2,3,4,5,6,7)
# arr = ('a', 'b', 'c', 'd')
#
# It = iter(arr);
# i = 0;
# while(i  < len(arr)):
#     print(next(It));
#     i += 1;

def func(n):
    m = n
    print("第", m - n + 1, "次调用_next_()")
    while n > 0 :
        print("第", m - n + 1, "次挂起")
        yield n
        n -= 1
        print("第", m - n, "次释放")
    print("第", m - n + 1,"次调用_next_()")


y = func(3)
for i in y:
    print("第", 4 - i,"次调用/循环")
