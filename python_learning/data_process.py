from matplotlib import pyplot as plt
import random

# import matplotlib
# matplotlib.rc("font",family = 'MicroSoft YaHei UI', whight = "bold", size = "larger")

# plt.rcParams['font.sans-serif'] = ["MicroSoft YaHei UI"]
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

1
2
3
4

x = range( 0, 120 )   #产生横坐标
y = [ random.randint( 20, 35 ) for i in range(120)]  #产生随机温度纵坐标


#设计清晰度和图片大小：
plt.figure( figsize = ( 15, 8 ), dpi = 80 )



plt.plot( x, y )  #画图

#调整x轴的刻度：
_x = x
# _xticks_labels = [ "hello,{}".format(i) for i in _x]
_xticks_labels = [ "10:{0}时".format(i) for i in range(60)]   #可以用rotation（旋转的度数）
_xticks_labels += [ "11:{0}AM".format(i) for i in range(60)]
plt.xticks( list(x)[::10], _xticks_labels[::10], rotation = 45 )

#调整y轴刻度：
# _y = y
_yticks_label = [ i for i in range( 20, 36 )]
plt.yticks( _yticks_label)


plt.show()        #展示






# import matplotlib.pyplot as plt  
  
# # 创建一个简单的线图  
# x = [1, 2, 3, 4, 5]  
# y = [1, 4, 2, 3, 7]  
# plt.plot(x, y)  
  
# # 设置x轴的刻度位置和标签  
# # 这里我们想要将刻度位置设置为1, 2.5, 4, 5，并将它们标记为'A', 'B', 'C', 'D'  
# # plt.xticks([1, 2.5, 4, 5], ['A', 'B', 'C', 'D'])  
  
# # 显示图表  
# plt.show()