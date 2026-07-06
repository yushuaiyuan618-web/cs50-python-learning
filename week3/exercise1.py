# =========================
# 题目 1：重复输入直到合法
# 要求：
# 写一个程序，让用户输入一个正整数 n。
#
# 如果用户输入的是 0 或负数，就一直重新输入。
# 只有当用户输入正整数时，才结束循环。
#
# 最后输出：
# You entered: n
#
# 示例：
# Number: -3
# Number: 0
# Number: 5
# You entered: 5
#
# 思考：
# 1. while 循环什么时候继续？
# 2. while 循环什么时候结束？
# 3. 可以用 while True + break 来写吗？
#
# 提示结构：
# while True:
#     n = int(input("Number: "))
#     if 条件满足:
#         break
# print(...)

while True:
    n = int(input("Number: "))
    if n > 0:
        break

print(n)