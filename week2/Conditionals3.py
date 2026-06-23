# Exercise 3: Grade System

# 目标：
# 输入成绩（0-100）

# 输出等级：
# 90-100 → A
# 80-89  → B
# 70-79  → C
# 60-69  → D
# <60    → F

score = int(input("What's your scores?"))
if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("E")