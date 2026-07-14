# ==================================
# 题目 1：随机抛硬币
# ==================================
#
# 要求：
# 使用 Python 自带的 random 库，随机输出：
#
# Heads
# 或
# Tails
#
# 每次运行程序，结果可能不同。
#
# 示例：
# Heads
#
# 或：
# Tails
#
# 需要用到：
# import random
# random.choice(...)
#
# 思考：
# 1. random 是什么？
# 2. choice 的中文意思是什么？
# 3. choice() 里面应该放一个字符串，还是一个列表？
#
# 提示：
#
# choices = ["Heads", "Tails"]
#
# 然后让 random 从 choices 中随机选择一个。

import random 
print(random.choice(["Heads", "Tails"]))