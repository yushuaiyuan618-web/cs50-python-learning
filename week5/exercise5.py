# ==================================
# 加分题：随机抽取学生
# ==================================
#
# 要求：
# 创建一个学生名单：
#
# students = ["Alice", "Bob", "Harry", "Ron", "Hermione"]
#
# 使用 random 库完成：
#
# 1. 随机抽取一名学生回答问题。
# 2. 随机打乱整个学生名单。
# 3. 输出打乱后的名单。
#
# 需要用到：
# random.choice()
# random.shuffle()
#
# 注意：
# random.shuffle() 会直接修改原来的列表。
#
# 示例：
# Selected: Ron
# New order: ['Harry', 'Alice', 'Ron', 'Bob', 'Hermione']

import random

students = ["Alice", "Bob", "Harry", "Ron", "Hermione"]

selected = random.choice(students)

random.shuffle(students)

print(f"Selected: {selected}")
print(f"New order: {students}")