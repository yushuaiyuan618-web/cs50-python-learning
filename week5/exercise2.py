# ==================================
# 题目 2：掷骰子模拟器
# ==================================
#
# 要求：
# 让用户输入一个正整数 times，表示掷骰子的次数。
#
# 每次随机产生一个 1 到 6 之间的整数，并输出。
#
# 示例：
# Times: 5
# 3
# 6
# 1
# 4
# 4
#
# 要求：
# 1. 使用 random 库。
# 2. 使用 for 循环。
# 3. 使用 random.randint()。
#
# 需要用到：
# import random
# range()
# random.randint(1, 6)
#
# 思考：
# 1. randint(1, 6) 会不会包括 1 和 6？
# 2. 用户输入 5，循环应该执行几次？
#
# 挑战：
# 在最后统计所有骰子点数的总和。
#
# 示例：
# Total: 18

import random

times = int(input("Times: "))

total = 0
for _ in range(times):
    dice = random.randint(1,6)
    print(dice)

    total = total + dice

print(f"Total: {total}")