# ==================================
# 题目 4：使用命令行参数打招呼
# ==================================
#
# 要求：
# 使用 sys 库读取命令行参数。
#
# 在终端中运行：
#
# python greet.py Harry
#
# 输出：
#
# Hello, Harry
#
# 如果没有输入名字：
#
# python greet.py
#
# 输出：
#
# Missing command-line argument
#
# 如果输入了两个或更多名字：
#
# python greet.py Harry Ron
#
# 输出：
#
# Too many command-line arguments
#
# 需要用到：
# import sys
# sys.argv
# len()
# if / elif / else
#
# 提示：
#
# sys.argv[0] 是 Python 文件名。
# sys.argv[1] 才是用户输入的第一个参数。
#
# 思考：
# 1. 运行 python greet.py Harry 时，
#    sys.argv 里面一共有几个元素？
#
# 2. 为什么名字 Harry 对应 sys.argv[1]，
#    而不是 sys.argv[0]？
#
# 3. 怎么用 len(sys.argv) 判断参数数量？

import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

print(f"Hello, {sys.argv[1]}")