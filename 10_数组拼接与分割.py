# ============================================================
# 第10章：数组拼接与分割 —— 把数组拼起来、拆开
# ============================================================
# 有时候你需要把两个数组"粘"在一起，或者把一个数组切成几块。
# 这些操作在数据预处理中非常常见。
#
# 拼接：就像把两张纸粘在一起（可以上下粘，也可以左右粘）
# 分割：就像把一张纸裁成几张小纸片

import numpy as np


# ============================================================
# 10.1 拼接 —— np.concatenate, np.vstack, np.hstack
# ============================================================
# concatenate 是最通用的拼接函数，但 vstack（垂直堆叠）和
# hstack（水平堆叠）更常用，因为名字更直观。

print("=" * 50)
print("10.1 拼接数组")

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

print(f"数组 a:\n{a}")
print(f"数组 b:\n{b}")

# 垂直拼接（上下堆叠）：vstack → 行数增加，列数不变
v_result = np.vstack([a, b])
print(f"\nnp.vstack([a, b]) —— 上下拼:\n{v_result}")
print(f"shape: {v_result.shape}")  # (4, 2)

# 水平拼接（左右堆叠）：hstack → 列数增加，行数不变
h_result = np.hstack([a, b])
print(f"\nnp.hstack([a, b]) —— 左右拼:\n{h_result}")
print(f"shape: {h_result.shape}")  # (2, 4)

# concatenate：通用拼接，需要指定 axis
# axis=0 → 沿行方向（上下拼），同 vstack
# axis=1 → 沿列方向（左右拼），同 hstack
c_result = np.concatenate([a, b], axis=0)
print(f"\nnp.concatenate([a,b], axis=0) —— 同 vstack:\n{c_result}")

c_result2 = np.concatenate([a, b], axis=1)
print(f"\nnp.concatenate([a,b], axis=1) —— 同 hstack:\n{c_result2}")


# ============================================================
# 10.2 一维数组的拼接
# ============================================================
print("\n" + "=" * 50)
print("10.2 一维数组的拼接")

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# 直接拼接
print(f"np.concatenate([x, y]): {np.concatenate([x, y])}")

# hstack 在一维数组上等价于 concatenate
print(f"np.hstack([x, y]): {np.hstack([x, y])}")

# 也可以堆叠成二维数组
# vstack 会把一维数组变成二维行
print(f"np.vstack([x, y]):\n{np.vstack([x, y])}")
# 结果：[[1, 2, 3],
#        [4, 5, 6]]

# column_stack：把一维数组变成二维的列
print(f"np.column_stack([x, y]):\n{np.column_stack([x, y])}")
# 结果：[[1, 4],
#        [2, 5],
#        [3, 6]]


# ============================================================
# 10.3 分割 —— np.split, np.vsplit, np.hsplit
# ============================================================
# 分割是拼接的反操作。把一个数组切成几块。

print("\n" + "=" * 50)
print("10.3 分割数组")

arr = np.arange(1, 13).reshape(3, 4)
print(f"原数组:\n{arr}")

# 水平分割（切成左右两半）：hsplit
# 参数：数组, 切几份（必须能整除！）
left, right = np.hsplit(arr, 2)
print(f"\nhsplit 切成2份:")
print(f"左边:\n{left}")
print(f"右边:\n{right}")

# 垂直分割（切成上下两半）：vsplit
# 3 行没法均分，我们用 6 行的数组
arr2 = np.arange(1, 25).reshape(6, 4)
print(f"\n新数组 (6x4):\n{arr2}")
top, bottom = np.vsplit(arr2, 2)
print(f"\nvsplit 切成2份:")
print(f"上面:\n{top}")
print(f"下面:\n{bottom}")

# 也可以指定切分点（不一定要均分）
# np.split(arr, [切分点], axis=方向)
arr3 = np.arange(1, 13).reshape(3, 4)
print(f"\n原数组 (3x4):\n{arr3}")
# 在第 1 行后切一刀，切成 1 行 + 2 行
pieces = np.split(arr3, [1], axis=0)
print(f"在第1行后切一刀:")
print(f"第1块:\n{pieces[0]}")
print(f"第2块:\n{pieces[1]}")


# ============================================================
# 10.4 实战：把数据拼成表格
# ============================================================
print("\n" + "=" * 50)
print("10.4 实战：构建数据表格")

# 假设你有三个特征：身高、体重、年龄
heights = np.array([170, 165, 180, 175])
weights = np.array([65, 55, 80, 70])
ages = np.array([20, 22, 21, 23])

# 用 column_stack 把三个一维数组拼成二维表格
# 每列代表一个特征，每行代表一个人
data = np.column_stack([heights, weights, ages])
print("数据表格（身高, 体重, 年龄）:")
print(data)
print(f"shape: {data.shape}")  # (4, 3)

# 反过来，把表格拆成各列
h, w, a = np.hsplit(data, 3)
print(f"\n拆回身高: {h.flatten()}")
print(f"拆回体重: {w.flatten()}")
print(f"拆回年龄: {a.flatten()}")


# ============================================================
# 本章总结
# ============================================================
print("\n" + "=" * 50)
print("【本章总结】")
print("""
拼接：
  np.vstack([a, b])           → 垂直堆叠（上下拼，行变多）
  np.hstack([a, b])           → 水平堆叠（左右拼，列变多）
  np.concatenate([a,b], axis=0) → 通用拼接，axis=0 同 vstack
  np.concatenate([a,b], axis=1) → 通用拼接，axis=1 同 hstack
  np.column_stack([x, y, z])  → 把多个一维数组拼成二维表格

分割：
  np.vsplit(arr, n)           → 垂直切成 n 份
  np.hsplit(arr, n)           → 水平切成 n 份
  np.split(arr, [切分点], axis) → 通用分割

记住：拼接时注意形状要匹配，否则会报错！
""")