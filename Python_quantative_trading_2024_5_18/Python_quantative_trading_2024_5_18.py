# import copy
# from collections.abc import MutableMapping
#
# class Entity(MutableMapping):
#     def __init__(self):
#         self._data = {}
#     def __setitem__(self,key,value):
#         # return self.__dict__.__setitem__(key,value)
#         self._data[key] = value
#     def __delitem__(self, key):
#         # return self.__dict__.__delitem__(key)
#         if key in self._data:
#             del self._data[key]
#         else:
#             print("Delete error!")
#     def __getitem__(self, key):
#         # return self._data.__getitem__(key)
#         return self._data.get(key)
#     def __iter__(self):
#         # return iter({ k: v for k,v in self.__dict__.items() if not k.startswith("_")})
#         return iter(self._data)
#     def __len__(self):
#         return len(self._data)
#     def __str__(self):
#         return str({k:v for k,v in self.__dict__.items() if not k.startswith("_")})
#     def __repr__(self):
#         return '{},D({})'.format(super(Entity,self).__repr__(),{k:v for k,v in self.__dict__.items() if not k.startswith("_")})
#     def copy(self):
#         return copy.copy(self)
#
# class Order(Entity):
#     def __init__(self,api):
#         super().__init__()
#         self._api = api
#         self.order_id: str = ""  #：委托单ID，对于一个用户的所有委托单，这个ID都是不重复的
#         self.exchange_order_id: str = "" #交易所单号
#         self.exchange_id: str = ""  #交易所
#         self.instrument_id: str = ""  #交易所内的合约代码
#         self.direction: str = ""  #下单方向：BUY Or SELL
#         self.offset: str = ""  #开仓标志，OPEN = 开仓，CLOSE = 平仓，CLOSETODAY = 平今
#         self.volume_orgin: int = 0  #总报单手数
#         self.volume_left: int = 0  #未成交手数
#         self.limit_price: float = float("nan")  #委托价格，仅当 price_type = LIMIT时有效
#         self.prince_type: str = ""   #价格类型：ANY = 市价， LIMIT = 限价
#         self.volume_condition: str = ""  #手数条件，ANY = 任何数量， MIN = 最小数量， ALL = 全部数量
#         self.time_condition: str = ""   #时间条件，IOC = 立即完成，否则撤销， GFS = 本节有效， GFD = 当日有效
#                                         # GTC = 撤销前有效， GFA = 集合竞价有效
#         self.insert_data_time: int = 0 #下单时刻的纳秒数，自Unix Epoch（1970-01-01 00:00:00 GMT）以来的纳秒数
#         self.last_msg: str = ""  #委托单状态信息
#         self.status: str = ""  #委托单状态，ALIVE = 有效，FINISHED = 已完成
#         self._this_session = False
#
#
#
# entity = Entity()
# print(entity)
# order = Order("api")
# print(order.volume_orgin)
# order["volume_orgin"] = 100
# print(order["volume_orgin"])
# print(order)


# def func2(y):
#     def func1(x):
#         return x**y
#     return func1
#
# f = func2(y = 3)
# print(f(x = 9))

# def func1(func):
#     def Cal_dou(x,y):
#         a = func(x,y)
#         print(a)
#         return a
#     return Cal_dou
#
# @func1
# def func2(x,y):
#     return x**y
# func2(2,3)
#
# ret = func1(func2)
# print(ret(2,3))


# from functools import wraps
# def decorator(func):
#     @wraps(func)
#     def wrapfunc(*args, **kwargs):
#         print("装饰器")
#         return func(*args,**kwargs)
#     return wrapfunc
#
# @decorator
# def func(*args,**kwargs):
#     pass

from functools import wraps
class A():
    def __init__(self,a: int = 5,b: int = 6):
        self.a = a
        self.b = b
    def __call__(self,func):
        @wraps(func)
        def wrapfunc(*args, **kwargs):  #一个判断大小的装饰函数
            print("传入了函数", func.__name__)
            if self.a >= self.b :
                print("a >= b")
            else:
                print("a < b")
            return func(*args, **kwargs)
        return wrapfunc

# @A(a = 5, b = 6)
@A
def func(x,y):   #func = A(a = 5,b = 6)(func)
    return x**y

C = func(3,4)

print()