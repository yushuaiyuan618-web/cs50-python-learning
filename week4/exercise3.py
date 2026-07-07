# =========================
# 题目 3：安全除法计算器
# =========================
#
# 要求：
# 写一个程序，让用户输入两个整数 x 和 y。
#
# 然后输出：
# x / y 的结果
#
# 但是要处理两种错误：
#
# 1. 如果用户输入的不是整数，要重新输入。
#    比如输入 hello、abc、3.5
#
# 2. 如果 y 输入的是 0，不能让程序崩溃。
#    因为除以 0 会报错。
#
# 示例 1：
# x: 10
# y: 2
# 10 / 2 = 5.0
#
# 示例 2：
# x: abc
# x: 10
# y: 0
# y cannot be 0
# y: 5
# 10 / 5 = 2.0
#
# 要求：
# 你可以写两个函数：
#
# def get_int(prompt):
#     ...
#
# def main():
#     ...
#
# 需要用到：
# try
# except ValueError
# ZeroDivisionError
# while True
#
# 提示：
#
# try:
#     result = x / y
# except ZeroDivisionError:
#     ...

def main():
    x = get_int("x: ")

    while True:
        y = get_int("y: ")
        try:
            result = x / y
        except ZeroDivisionError:
            print("y cannot be 0")
        else:
            break

    print(f"{x} / {y} = {result}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
