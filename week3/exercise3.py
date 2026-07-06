# =========================
# 题目 3：统计元音字母
# =========================
#
# 要求：
# 让用户输入一句英文。
#
# 统计这句话中有多少个元音字母。
#
# 元音字母包括：
# a, e, i, o, u
#
# 大写和小写都要算。
#
# 示例：
# Text: Hello World
# Vowels: 3
#
# 因为 Hello World 里面有：
# e, o, o
#
# 思考：
# 1. 怎么一个一个检查字符串里的字母？
# 2. 怎么判断这个字母是不是元音？
# 3. 怎么让大写字母也能被统计？
#
# 提示：
#
# text = input("Text: ")
# count = 0
#
# for letter in text:
#     if letter.lower() in "aeiou":
#         ...
#
# print(...)

text = input("Text: ")
count = 0

for letter in text:
    if letter.lower() in "aeiou":
        count = count + 1

print("Vowels: ", count)
