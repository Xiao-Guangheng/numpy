# ============================================================
# 第6章：通用函数（ufunc）—— 真正的高速运算
# ============================================================
# ufunc 是 NumPy 的核心概念之一，全称是"通用函数"
#（Universal Function）。简单说，就是能对数组的每个元素
# 同时进行操作的函数。
#
# 你不需要理解 ufunc 的底层实现，只需要知道：
# 能用 ufunc 就别用 for 循环，因为 ufunc 底层是 C 语言写的，
# 速度不是一个级别。

import numpy as np


# ============================================================
# 6.1 什么是 ufunc？和普通函数有什么区别？
# ============================================================
# 普通 Python 函数：一次只能处理一个数字
# ufunc：一次处理整个数组的所有元素，速度快几十倍

print("=" * 50)
print("6.1 认识 ufunc")

arr = np.array([1, 4, 9, 16, 25])

# 这些你之前见过的都是 ufunc：
print(f"np.sqrt(arr) = {np.sqrt(arr)}")  # 对每个元素开平方
print(f"np.exp(arr)  = {np.exp(arr)}")   # 对每个元素求 e 的幂

# 甚至加减乘除也是 ufunc 实现的：
print(f"np.add([1,2], [3,4]) = {np.add([1, 2], [3, 4])}")
# 等价于 [1, 2] + [3, 4]，但 np.add 是 ufunc，可以传更多参数


# ============================================================
# 6.2 一元 ufunc —— 输入一个数组，输出一个数组
# ============================================================
# 这些函数对数组的每个元素做独立的计算。

print("\n" + "=" * 50)
print("6.2 一元 ufunc（一个输入，一个输出）")

arr = np.array([-1.5, 0, 2.3, 3.7, -4.1])

# 数学函数
print(f"np.abs(arr)    = {np.abs(arr)}")      # 绝对值
print(f"np.sqrt(np.abs(arr)) = {np.sqrt(np.abs(arr))}")  # 平方根
print(f"np.square(arr) = {np.square(arr)}")    # 平方
print(f"np.sign(arr)   = {np.sign(arr)}")      # 符号（正数=1, 0=0, 负数=-1）

# 取整函数
arr2 = np.array([1.2, 2.7, 3.5, 4.1])
print(f"\nnp.floor(arr2) = {np.floor(arr2)}")  # 向下取整 → [1, 2, 3, 4]
print(f"np.ceil(arr2)  = {np.ceil(arr2)}")     # 向上取整 → [2, 3, 4, 5]
print(f"np.round(arr2) = {np.round(arr2)}")    # 四舍五入 → [1, 3, 4, 4]
print(f"np.rint(arr2)  = {np.rint(arr2)}")     # 也是四舍五入

# 指数和对数
print(f"\nnp.exp([1, 2])    = {np.exp([1, 2])}")       # e^x
print(f"np.log([1, np.e])  = {np.log([1, np.e])}")     # ln(x)
print(f"np.log2([1, 2, 4]) = {np.log2([1, 2, 4])}")    # log2(x)
print(f"np.log10([1, 10, 100]) = {np.log10([1, 10, 100])}")  # log10(x)

# 三角函数
print(f"\nnp.sin([0, np.pi/2]) = {np.sin([0, np.pi/2])}")
print(f"np.cos([0, np.pi])    = {np.cos([0, np.pi])}")


# ============================================================
# 6.3 二元 ufunc —— 输入两个数组，输出一个数组
# ============================================================
# 这些函数对两个数组的对应元素做运算。

print("\n" + "=" * 50)
print("6.3 二元 ufunc（两个输入，一个输出）")

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(f"np.add(a, b)      = {np.add(a, b)}")       # 加法
print(f"np.subtract(a, b) = {np.subtract(a, b)}")   # 减法
print(f"np.multiply(a, b) = {np.multiply(a, b)}")   # 乘法
print(f"np.divide(a, b)   = {np.divide(a, b)}")     # 除法
print(f"np.power(a, 2)    = {np.power(a, 2)}")      # 幂运算
print(f"np.maximum(a, b)  = {np.maximum(a, b)}")    # 取两个中较大的
print(f"np.minimum(a, b)  = {np.minimum(a, b)}")    # 取两个中较小的

# np.maximum 和 np.minimum 特别有用：
# 比如你想把数组中小于 0 的值都变成 0：
data = np.array([-3, 5, -1, 8, 0, -2])
clipped = np.maximum(data, 0)  # 所有负数变成 0
print(f"\n原数据: {data}")
print(f"np.maximum(data, 0): {clipped}")


# ============================================================
# 6.4 ufunc 的 out 参数 —— 把结果存到指定数组
# ============================================================
# 默认情况下，ufunc 返回一个新数组。但如果你已经有一个
# 现成的数组，可以让 ufunc 把结果直接写进去，省内存。

print("\n" + "=" * 50)
print("6.4 ufunc 的 out 参数")

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# 预先创建一个空数组来接结果
result = np.empty(4, dtype=np.int32)

# 把结果直接写入 result，不创建新数组
np.add(a, b, out=result)
print(f"结果直接写入 result: {result}")

# 这对大数组很有用，避免频繁分配内存


# ============================================================
# 6.5 常用 ufunc 速查表
# ============================================================
print("\n" + "=" * 50)
print("6.5 常用 ufunc 速查")

print("""
【一元 ufunc】（输入一个数组）
  np.abs(x)        → 绝对值
  np.sqrt(x)       → 平方根
  np.square(x)     → 平方
  np.exp(x)        → e^x
  np.log(x)        → 自然对数
  np.log2(x)       → 以 2 为底的对数
  np.log10(x)      → 以 10 为底的对数
  np.sin/cos/tan   → 三角函数
  np.floor(x)      → 向下取整
  np.ceil(x)       → 向上取整
  np.round(x)      → 四舍五入
  np.sign(x)       → 符号（-1, 0, 1）

【二元 ufunc】（输入两个数组）
  np.add(a, b)     → 加法
  np.subtract(a,b) → 减法
  np.multiply(a,b) → 乘法
  np.divide(a,b)   → 除法
  np.power(a,b)    → 幂运算
  np.maximum(a,b)  → 逐元素取较大值
  np.minimum(a,b)  → 逐元素取较小值
""")


# ============================================================
# 本章总结
# ============================================================
print("=" * 50)
print("【本章总结】")
print("""
ufunc 就是能对数组每个元素同时操作的"超级函数"。
你已经在用的 +, -, *, /, np.sqrt, np.exp 都是 ufunc。

关键要点：
  - ufunc 底层是 C 语言，速度极快
  - 能用 ufunc 就别用 for 循环
  - np.maximum(arr, 0) 可以把所有负数归零（非常实用）
  - out 参数可以把结果写入已有数组，省内存
""")