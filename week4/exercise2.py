# =========================
# 题目 2：写一个 get_int 函数
# =========================
#
# 要求：
# 把“安全输入整数”封装成一个函数：
#
# def get_int(prompt):
#     ...
#
# 然后在 main() 里面调用它。
#
# 程序效果：
#
# What's x? abc
# What's x? 3.5
# What's x? 10
# x is 10
#
# 你最终代码结构应该类似：
#
# def main():
#     x = get_int("What's x? ")
#     print(f"x is {x}")
#
#
# def get_int(prompt):
#     ...
#
#
# main()
#
# 思考：
# 1. prompt 是什么？
# 2. input(prompt) 是什么意思？
# 3. 为什么输入正确后要 return？
# 4. 如果 except 里面写 pass，会发生什么？
#
# 要求：
# 输入错误时不要报错，重新输入。
# 输入正确时返回这个整数。

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