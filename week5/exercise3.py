# ==================================
# 题目 3：学生成绩统计
# ==================================
#
# 要求：
# 给定一个成绩列表：
#
# scores = [85, 92, 76, 88, 95]
#
# 使用 statistics 库计算并输出：
#
# 1. 平均分
# 2. 中位数
#
# 示例：
# Average: 87.2
# Median: 88
#
# 需要用到：
# import statistics
#
# statistics.mean(...)
# statistics.median(...)
#
# 思考：
# 1. mean 是什么意思？
# 2. median 是什么意思？
# 3. mean() 和 median() 需要自己写循环计算吗？
#
# 挑战：
# 再使用 Python 自带的 max() 和 min() 输出：
#
# Highest: 95
# Lowest: 76

import statistics

scores = [85, 92, 76, 88, 95]

average = statistics.mean(scores)
median = statistics.median(scores)
highest = max(scores)
lowest = min(scores)

print(f"Average: {average}")
print(f"Median: {median}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
