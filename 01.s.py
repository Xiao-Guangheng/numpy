import numpy as np

table = np.array([[1,2,3,4],
[5,6,7,8],
[9,10,11,12,13]])

print(table)

#指定数据类型

arr_int = np.array([1,2,3],dtype=np.int32)
#int32表示32位整数，四个字节，范围挺大的，如果你想存更大范围的整数，可以用int64，或者float64表示浮点数
#数据很多的失手类型越小越省内存，但是范围也更小，默认int64,float64

#创建占位数组

#全0

empty_ground = np.zeros((3,4))
#这时候要用zeros

#全1

ones_ground = np.ones((2,3))
#全1 用于做基底，就是在矩阵做乘法的时候不会改变值，适合做基底

#指定值
all_ground = np.full((2,3),7)


#等差数列  arange linspace
arange_array = np.arange(0,stop=20,step=2)
#三个参数分别是起始值，终止值，步长，生成一个等差数列，左闭右开区间
#只有一个默认参数
sdf = np.arange(10)

linspace_array = np.linspace(start=0,stop=1,num=5)
#起始值是0，终止值是1，生成5个等差数列，5表示生成的数值个数，默认是50个


#单位矩阵
#对角线全是1，其余都是0
#任何矩阵乘以这个矩阵都还是它自己

I= np.eye(3)
#只有一个参数，表示单位矩阵的行数和列数，默认是方阵

#对角矩阵
#对角线是指定的值，其余都是0
diag_matrix = np.diag([1, 2, 3])
#可以反过来用，提取矩阵的对角线
print(np.diag(diag_matrix))

#复制数组

original = np.array([1, 2, 3, 4, 5])
arrr2 =original
#这样只是把数组改名了，而不是创建新的数组，没有复制数据本身

arr3 = original.copy()
arr3[0] = 999
#x相当于创建了一个副本


#复用已有数组的形状
arr4 = np.array([21,12,32,23],
[43,34,54,45])

result = np.zeros_like(arr4)
#创建了一个全0的矩阵，形状和arr4一样，数据类型也一样
#还有ones_like,full_like都是一样的
