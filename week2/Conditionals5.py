# Exercise 5: Number Analyzer

# 目标：
# 输入一个整数

# 输出：
# 1. 是 positive / negative / zero
# 2. 是 even / odd（如果不是 zero）

# 示例：
# 4 → positive, even
# -3 → negative, odd
# 0 → zero

x = int(input("x: "))
def is_positive(x):
    return x > 0
def is_negative(x):
    return x < 0
def is_even(x):
    return x % 2 == 0

if x == 0:
    print("zero")

elif is_positive(x):
    if is_even(x):
        print("positive,even")
    else:
        print("positive,odd")
elif is_negative(x):
    if is_even(x):
        print("negative,even")
    else:
        print("negative,odd")
