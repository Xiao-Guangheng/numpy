# ============================================================
# 第12章：随机数 —— 让计算机帮你"掷骰子"
# ============================================================
# 随机数在科学计算中无处不在：初始化神经网络权重、随机采样、
# 数据增强、蒙特卡洛模拟……都离不开它。
#
# NumPy 的随机数模块 np.random 提供了丰富的随机数生成功能。
# 注意：计算机生成的"随机数"其实是伪随机数——由算法生成，
# 看起来随机，但给定相同的种子（seed），结果可复现。

import numpy as np


# ============================================================
# 12.1 设置随机种子 —— np.random.seed
# ============================================================
# 为什么需要种子？因为"可复现"是科学计算的基本要求。
# 你的实验结果应该能被别人（包括你自己）复现。
# 设置相同的 seed，就能得到相同的随机数序列。

print("=" * 50)
print("12.1 随机种子：让随机变得"可预测"")

np.random.seed(42)
print("seed=42, 第一次:", np.random.rand(3))

np.random.seed(42)
print("seed=42, 第二次:", np.random.rand(3))  # 和第一次一样！

np.random.seed(99)
print("seed=99, 第一次:", np.random.rand(3))  # 不同的种子，不同的结果

# 不设置种子：每次运行结果都不同
print("不设置种子:", np.random.rand(3))

# 最佳实践：程序开头设置一次种子即可
np.random.seed(2024)  # 之后所有随机操作都可复现


# ============================================================
# 12.2 基础随机数生成
# ============================================================
# 三种最常用的随机数生成器：

print("\n" + "=" * 50)
print("12.2 基础随机数生成")

# 1. rand(d0, d1, ...)：生成 [0, 1) 之间的均匀分布随机数
print("np.random.rand(5):", np.random.rand(5))
print("np.random.rand(3, 2):\n", np.random.rand(3, 2))

# 2. randn(d0, d1, ...)：生成标准正态分布（均值为0，标准差为1）的随机数
# 类比：人的身高、智商大致服从正态分布，randn 就是模拟这种"钟形曲线"
print("\nnp.random.randn(5):", np.random.randn(5))
print("np.random.randn(3, 2):\n", np.random.randn(3, 2))

# 3. randint(low, high, size)：生成指定范围 [low, high) 的整数
print("\nnp.random.randint(1, 7, 10):", np.random.randint(1, 7, 10))
print("  相当于掷 10 次骰子")
print("np.random.randint(0, 100, (3, 4)):\n", np.random.randint(0, 100, (3, 4)))


# ============================================================
# 12.3 随机选择与打乱 —— choice 和 shuffle
# ============================================================
print("\n" + "=" * 50)
print("12.3 随机选择与打乱")

# randint 只能生成数字范围内的随机整数。
# 如果你想从已有的列表/数组中随机抽，用 choice。

students = np.array(["Alice", "Bob", "Charlie", "David", "Eve", "Frank"])

# 随机抽 1 个
print(f"抽一个人: {np.random.choice(students)}")

# 随机抽 3 个（不重复，默认 replace=False? 不，默认 replace=True！）
# 注意：默认 replace=True 意味着可能抽到重复的！
print(f"抽 3 个（可重复）: {np.random.choice(students, 3)}")
print(f"抽 3 个（不重复）: {np.random.choice(students, 3, replace=False)}")

# 带概率的随机抽取
# 比如：抽奖，一等奖概率 10%，二等奖 30%，三等奖 60%
prizes = np.array(["一等奖", "二等奖", "三等奖"])
probs = np.array([0.1, 0.3, 0.6])
draws = np.random.choice(prizes, 100, p=probs)
print(f"\n100 次抽奖结果（按概率）:")
print(f"  一等奖: {(draws == '一等奖').sum()} 次")
print(f"  二等奖: {(draws == '二等奖').sum()} 次")
print(f"  三等奖: {(draws == '三等奖').sum()} 次")

# shuffle：随机打乱数组（原地修改！）
arr = np.arange(10)
print(f"\n打乱前: {arr}")
np.random.shuffle(arr)
print(f"打乱后: {arr}")
# 注意 shuffle 是原地修改，不返回新数组！


# ============================================================
# 12.4 更多分布：看情况用
# ============================================================
print("\n" + "=" * 50)
print("12.4 其他分布")

# 有时候你需要特定分布的随机数：
# np.random.uniform(low, high, size)    → [low, high) 均匀分布
# np.random.normal(mean, std, size)      → 正态分布（指定均值和标准差）
# np.random.exponential(scale, size)     → 指数分布
# np.random.binomial(n, p, size)        → 二项分布

print("均匀分布 [10, 20):", np.random.uniform(10, 20, 5))
print("正态分布 (均值=70, 标准差=15):", np.random.normal(70, 15, 5))
print("  模拟学生考试成绩，均值 70，标准差 15")


# ============================================================
# 12.5 实战：模拟一个简单的实验
# ============================================================
print("\n" + "=" * 50)
print("12.5 实战：模拟抛硬币实验")

# 抛 1000 次硬币，统计正面朝上的次数
# 0 = 反面，1 = 正面
np.random.seed(42)
coin_flips = np.random.randint(0, 2, 1000)
heads = (coin_flips == 1).sum()
tails = (coin_flips == 0).sum()
print(f"抛 1000 次硬币:")
print(f"  正面: {heads} 次 ({heads/1000*100:.1f}%)")
print(f"  反面: {tails} 次 ({tails/1000*100:.1f}%)")
print(f"  结论：接近 50%，符合预期！")


# ============================================================
# 本章总结
# ============================================================
print("\n" + "=" * 50)
print("【本章总结】")
print("""
  np.random.seed(n)              → 设置随机种子（保证可复现）
  np.random.rand(d0, d1, ...)    → [0, 1) 均匀分布
  np.random.randn(d0, d1, ...)   → 标准正态分布（均值0，标准差1）
  np.random.randint(low, high, size) → 指定范围整数
  np.random.choice(arr, n)       → 从数组中随机抽 n 个
  np.random.shuffle(arr)         → 原地打乱数组
  np.random.uniform(a, b, size)  → [a, b) 均匀分布
  np.random.normal(mean, std, size) → 正态分布

关键提醒：
  1. 科学计算时一定要设置种子！
  2. choice 默认 replace=True（可重复），注意是否需要 replace=False
  3. shuffle 是原地修改，不返回新数组
""")