# Exercise 4: Weather Checker

# 目标：
# 输入温度（整数）

# 输出：
# >30 → Hot
# 20-30 → Warm
# 10-19 → Cool
# <10 → Cold

temp = int(input("What's the temperature?"))
if temp > 30:
    print("Hot")
elif temp >=20:
    print("Warm")
elif temp >=10:
    print("Cool")
else:
    print("Cold")
    