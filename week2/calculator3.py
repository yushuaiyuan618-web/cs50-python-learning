# Exercise 3: Number Formatting

# 目标：
# 1. 输入一个数字（可能很大）
# 2. 输出：
#    - 千分位格式（,）
#    - 保留 2 位小数

# 示例：
# input: 1000000
# output: 1,000,000.00


# TODO:
# 1. 输入数字
# 2. 转 float
# 3. 使用 f-string 格式化输出
#    提示：{:,.2f}


n = float(input("N: "))
print(f"output = {n:,.2f}")
