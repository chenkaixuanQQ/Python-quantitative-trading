from  matplotlib import pyplot as plt
import random

arr = [ random.randint(20,35) for i in range (120)]

my_time = range(120)


#设置图片大小：
plt.figure(figsize = (20,8),dpi = 80)

plt.xticks

plt.plot(my_time,arr)
plt.show()
