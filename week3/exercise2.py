# =========================
# 题目 2：打印右对齐金字塔
# =========================
#
# 要求：
# 让用户输入一个高度 height。
#
# height 必须在 1 到 8 之间。
# 如果输入不合法，就一直重新输入。
#
# 然后打印一个由 # 组成的右对齐金字塔。
#
# 示例：
# Height: 4
#    #
#   ##
#  ###
# ####
#
# 思考：
# 假设 height = 4：
#
# 第 1 行：3 个空格，1 个 #
# 第 2 行：2 个空格，2 个 #
# 第 3 行：1 个空格，3 个 #
# 第 4 行：0 个空格，4 个 #
#
# 规律：
# 第 i 行：
# 空格数量 = height - i
# # 数量 = i
#
# 提示：
#
# for i in range(1, height + 1):
#     print(...)

while True:
    height = int(input("Height: "))
    if 1 <= height <=8:
        break

for i in range(1, height + 1):
    spaces = height - i
    hashes = i
    print(" "*spaces + "#"*hashes)
