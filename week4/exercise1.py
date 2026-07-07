# =========================
# 题目 1：安全输入整数
# =========================
# 要求：
# 写一个程序，让用户输入一个整数 x。
#
# 如果用户输入的不是整数，比如：
# hello
# 3.14
# abc
#
# 程序不能崩溃，而是重新让用户输入。
#
# 只有当用户输入合法整数时，才输出：
# x is 数字
#
# 示例：
# What's x? cat
# What's x? hello
# What's x? 5
# x is 5
#
# 要求你使用：
# try
# except ValueError
# while True
#
# 提示：
#
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         ...
#     else:
#         ...

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()