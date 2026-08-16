# ============================================================
# 第11章：文件读写 —— 把数组存到硬盘、再读回来
# ============================================================
# 数据不可能永远待在内存里。你需要把计算结果保存到文件，
# 下次再读回来继续用。NumPy 提供了两种主要方式：
#
#   1. 二进制格式（.npy / .npz）—— NumPy 专用，快、省空间
#   2. 文本格式（.txt / .csv）—— 人类可读，通用，但慢
#
# 选择哪种？如果用 NumPy 读写的，用 .npy；如果数据要
# 在 Excel 或其他程序里打开，用 .csv。

import numpy as np
import os

# 输出目录（避免污染工作区）
OUTPUT = "d:/Learn/py/numpy/output"
os.makedirs(OUTPUT, exist_ok=True)


# ============================================================
# 11.1 二进制格式：np.save 和 np.load
# ============================================================
# 这是 NumPy 最推荐的方式。保存成 .npy 文件，读回来时
# 形状、dtype 全部保留，不会丢失信息。

print("=" * 50)
print("11.1 二进制格式 .npy")

# 创建一些数据
arr = np.arange(12).reshape(3, 4)
print(f"原数组:\n{arr}")
print(f"  dtype: {arr.dtype}, shape: {arr.shape}")

# 保存——就这么简单
np.save(OUTPUT + "/my_array.npy", arr)
print(f"\n已保存到 {OUTPUT}/my_array.npy")

# 读回来
loaded = np.load(OUTPUT + "/my_array.npy")
print(f"\n读回来的数组:\n{loaded}")
print(f"  dtype: {loaded.dtype}, shape: {loaded.shape}")
# 完全一致！


# ============================================================
# 11.2 保存多个数组：np.savez 和 np.savez_compressed
# ============================================================
# 如果你有好几个数组想一起保存，用 savez。
# 它会创建一个 .npz 文件，里面可以放多个数组。

print("\n" + "=" * 50)
print("11.2 保存多个数组 .npz")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])
c = np.eye(3)

# 命名保存
np.savez(OUTPUT + "/my_arrays.npz", arr_a=a, arr_b=b, matrix=c)
print("已保存 3 个数组到 my_arrays.npz")

# 读回来——.npz 读回来像个字典
data = np.load(OUTPUT + "/my_arrays.npz")
print(f"文件中有哪些数组: {list(data.keys())}")
print(f"arr_a: {data['arr_a']}")
print(f"arr_b: {data['arr_b']}")
print(f"matrix:\n{data['matrix']}")

# savez_compressed：压缩版，文件更小
np.savez_compressed(OUTPUT + "/my_arrays_compressed.npz", arr_a=a, arr_b=b)
print(f"\n已保存压缩版到 my_arrays_compressed.npz")


# ============================================================
# 11.3 文本格式：np.savetxt 和 np.loadtxt
# ============================================================
# 文本格式（.csv, .txt）的优点是可以在 Excel 或记事本中打开。
# 缺点是慢、占空间大、精度可能丢失。

print("\n" + "=" * 50)
print("11.3 文本格式 .txt / .csv")

data = np.array([[1.5, 2.3, 3.7],
                 [4.2, 5.1, 6.8],
                 [7.9, 8.4, 9.0]])

# 保存为 CSV（逗号分隔）
np.savetxt(OUTPUT + "/data.csv", data, delimiter=",", fmt="%.2f",
           header="col1,col2,col3", comments="")
print("已保存 CSV 文件")

# 读回 CSV
csv_data = np.loadtxt(OUTPUT + "/data.csv", delimiter=",", skiprows=1)
print(f"从 CSV 读回:\n{csv_data}")

# 没有 header 的简单文本
scores = np.array([85, 92, 78, 60, 95])
np.savetxt(OUTPUT + "/scores.txt", scores, fmt="%d")
print(f"\n已保存成绩到 scores.txt")
read_scores = np.loadtxt(OUTPUT + "/scores.txt")
print(f"读回成绩: {read_scores}")


# ============================================================
# 11.4 处理复杂文本文件：np.genfromtxt
# ============================================================
# 真实世界的数据往往不完美：有缺失值、有注释行、有奇怪的格式。
# genfromtxt 是 loadtxt 的"升级版"，能处理这些情况。

print("\n" + "=" * 50)
print("11.4 genfromtxt —— 处理"脏"数据")

# 模拟一个有缺失值的数据文件
messy_content = """name,math,english,physics
Alice,85,92,78
Bob,60,NA,88
Charlie,95,89,NA
"""
with open(OUTPUT + "/messy.csv", "w", encoding="utf-8") as f:
    f.write(messy_content)

# genfromtxt 可以处理缺失值（NA 会变成 nan）
data = np.genfromtxt(OUTPUT + "/messy.csv", delimiter=",",
                     skip_header=1,          # 跳过标题行
                     dtype=float,            # 指定数据类型
                     filling_values=0)       # 缺失值填 0
print("处理后的数据:")
print(data)
# 注意：'NA' 被自动识别为缺失值，可以用 filling_values 填充


# ============================================================
# 本章总结
# ============================================================
print("\n" + "=" * 50)
print("【本章总结】")
print("""
选择哪种格式？
  二进制 (.npy/.npz) → 推荐！快、省空间、保精度。NumPy 专用。
  文本 (.txt/.csv)   → 需要给人看或用 Excel 打开时用。

常用函数：
  np.save("file.npy", arr)      → 保存单个数组
  np.load("file.npy")           → 读取单个数组
  np.savez("file.npz", a=x, b=y)→ 保存多个数组（命名）
  np.savetxt("file.csv", arr)   → 保存为文本
  np.loadtxt("file.csv")        → 读取文本
  np.genfromtxt("file.csv")     → 读取文本（能处理缺失值）

记住：文件路径要对！如果文件不存在，读操作会报错。
""")