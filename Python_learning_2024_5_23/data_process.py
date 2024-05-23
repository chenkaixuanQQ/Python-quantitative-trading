# import time
# t0 = time.time()
# import numpy as np


# array = np.array([[1,2,3], 
#                   [2,3,4]])
# print(array)
# print("number of dimention: ", array.ndim)
# print("shape: ", array.shape)
# print("size: ", array.size)
# time.sleep(1)
# print(time.time() - t0)


# import numpy as np

# arr = np.array([2, 3, 4], dtype = np.int64)
# print([1,2,3])
# print(arr)
# print(arr.dtype)

# zer = np.zeros( (4,5) )
# print(zer)

# one = np.ones( (4, 5) )
# print( one )

# ran = np.arange( 10, 21, 2)  #（起始位置， 终止位置， 步长）
# print(ran)

# sor = np.arange(15).reshape((3,5))  #不写初始位置，默认从0开始，且不含尾
# print(sor)

# Lin = np.linspace( 2, 10, 10)   #包头包尾
# print(Lin)




import numpy as np

# a = np.array([10,22,3,4])
# b = np.arange(4)

# print(a - 1)
# print(a - b)

# print(b)
# print(b < 3)
# print(a[b < 3])

arr1 = np.arange(4).reshape((2,2))
arr2 = np.arange(1,5).reshape((2,2))

# ret = arr1.dot(arr2)
# print(arr1)
# print(arr2)
# print(ret)

print(arr1)
# print(arr1.mean())
# print(np.mean(arr1))
# print(np.average(arr1))
# print(np.median(arr1))
# print(np.cumsum(arr1))
print(np.diff(arr1))


nzeoh,nzeol = np.nonzero(arr1)
print(nzeoh)
print(nzeol)
for i,j in zip(nzeoh,nzeol):
    print(arr1[i,j])
