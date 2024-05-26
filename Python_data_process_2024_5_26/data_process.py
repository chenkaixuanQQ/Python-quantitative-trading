from matplotlib import pyplot as plt



x = range(2,26,2)
y = [15,13,14,5,17,20,25,26,26,24,22,18]


#设置图片大小：
fig = plt.figure( figsize = ( 15, 8 ), dpi = 80 )

#绘图：
plt.plot( x, y )

#设置刻度：
plt.xticks( x )
plt.yticks( range( min(y) ,max(y) + 1) )


#保存图片:
# plt.savefig("./test.png")
# plt.savefig("./test.svg")

plt.show()
