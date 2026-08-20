import numpy as np

#数组的属性

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print({arr.shape})
print({arr.shape[0]}) #输出行数，就是shape的第一个元素
print({arr.shape[1]}) #输出列数，就是shape的第二个元素

#多维数组也是一样的

#一维数组：ndim
#一维数组其实就等于len(shape)，比如shape=(3,4)时ndim=2
# 这样ndim的用法还有就是输出数组的维度数

# size
print({arr.size}) #输出数组里一共有多少个元素
# 这里会输出 12，因为shape=(3,4)，所以3*4=12

# dtype
print({arr.dtype}) #输出数组里元素的数据类型

arr1 = np.array([1.1,1.2,1.3])
print({arr1.dtype}) #输出float64，因为数组里元素都是浮点数

# 为什么这里需要关心dtype,因为数据类型决定了每个元素占的内存，能存到什么范围

#数据转换类型，astype
arr2 = arr.astype(np.float32)
print({arr2.dtype}) #输出float32