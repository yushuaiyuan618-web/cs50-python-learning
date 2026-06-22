# Exercise 1: Basic Calculator

# 目标：
# 1. 输入两个数字（可以是 float）
# 2. 计算：和、差、积
# 3. 使用 f-string 输出结果

# 示例：
# x: 3
# y: 2
# sum = 5
# difference = 1
# product = 6


# TODO:
# 1. 输入 x
# 2. 输入 y
# 3. 转换数据类型（float）
# 4. 计算结果
# 5. 使用 print + f-string 输出

x = float(input("x: "))
y = float(input("y: "))
total = x + y
difference = x - y
product = x * y
print(f"sum = {total}")
print(f"difference = {difference}")
print(f"product = {product}")

