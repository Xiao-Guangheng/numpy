import numpy as np

#数组之间的运算
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a+b)   # [11 22 33 44]
print(a-b)   # [-9 -18 -27 -36]
print(a*b)   # [10 40 90 160]
print(a/b)   # [0.1 0.1 0.1 0.1]
#逐数字运算

#列表的话会直接拼接两个数组

#数组与标量的运算，相当于做一个广播，把标量广播到数组的每个元素上

print(a+10)   # [11 12 13 14]
print(a*2)    # [2 4 6 8]

scores = np.array([85, 92, 78, 95, 88])
adjusted = scores + 5
#实际应用场景里面就是把所有分数加5

#归1化操作

n =(scores - np.min(scores)) / (np.max(scores) - np.min(scores))
#所有数据都减去最小值，然后除以最大值与最小值的差，得到的数据都在0~1之间

#比较运算，产生布尔数组
arr1=np.array([1, 2, 3, 4])
print(arr1>2)   # [False False  True  True]
print(arr1==3)  # [False False  True False]
print(arr1!=4)  # [ True  True  True False]

#用布尔数组把符合要求的元素筛选出来
print(arr1[arr1>2])  # [3 4]

arr2= np.array([1,3,2,4])
print(arr1>arr2)  # [False False  True False]

names  = np.array(['小明', '小红', '小刚', '小华'])
scores = np.array([85, 92, 78, 95])

# 找出成绩大于 85 分的人的名字
names[scores > 85]   # ['小红', '小华']
#先得到一个布尔数组，然后用这个布尔数组去索引名字数组，就可以得到成绩大于85分的人的名字
#但是形状必须相同

#矩阵乘法
A=np.array([[1, 2], [3, 4]])
B=np.array([[5, 6], [7, 8]])
print(A * B)  # 逐元素相乘,这不是矩阵乘法
print(A @ B)  # 矩阵乘法

#关于矩阵的乘法是线性代数的内容

#三种等价写法
np.dot(A, B)  # 矩阵乘法
np.matmul(A, B)  # 矩阵乘法
A @ B  # 矩阵乘法
#主要就用@就行

#常用数学函数
arr = np.array([1, 4, 9, 16])

print(f"np.sqrt(arr) = {np.sqrt(arr)}")     # 平方根
print(f"np.exp([1,2]) = {np.exp([1, 2])}")  # e 的幂
print(f"np.log([1, np.e]) = {np.log([1, np.e])}")  # 自然对数
print(f"np.sin([0, np.pi/2]) = {np.sin([0, np.pi/2])}") # 正弦
print(f"np.abs([-1, -2, 3]) = {np.abs([-1, -2, 3])}")  # 绝对值
print(f"np.round([1.4, 2.7]) = {np.round([1.4, 2.7])}") # 四舍五入
print(f"np.floor([1.9, 2.1]) = {np.floor([1.9, 2.1])}") # 向下取整
print(f"np.ceil([1.1, 2.8]) = {np.ceil([1.1, 2.8])}")   # 向上取整

np.e
np.pi/2

#原地运算
arr2 = np.array([1, 2, 3, 4])
arr2 += 1  # 相当于 arr2 = arr2 + 1
#这样写不会创建新的数组
arr2 = arr2 +1 #这样写会创建一个新的数组，然后再赋值给arr2

import time
n = 1000000
#用一个循环来计算平方根，测试时间
start =time.time()
result_py = [x**0.5 for x in range(n)]
py_time = time.time() - start

#来看看numpy的速度
start = time.time()
result_np = np.sqrt(np.arange(n))
np_time = time.time() - start

print(f"Python time: {py_time:.10f}s, NumPy time: {np_time:.10f}s")