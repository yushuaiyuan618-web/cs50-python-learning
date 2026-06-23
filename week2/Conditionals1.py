# Exercise 1: Positive or Negative

# 目标：
# 输入一个数字
# 判断它是：
# positive / negative / zero

# 示例：
# input: 5 → positive
# input: -3 → negative
# input: 0 → zero

x = float(input("x: "))



def is_positive(x):
    return x > 0
def is_negative(x):
    return x < 0

if is_positive(x):
    print("positive")
elif is_negative(x):
    print("negative")
else:
    print("zero")