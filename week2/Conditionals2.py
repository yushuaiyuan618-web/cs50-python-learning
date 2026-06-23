# Exercise 2: Divisible by 3

# 目标：
# 输入一个整数
# 判断：
# 是否能被 3 整除

# 输出：
# "Yes" 或 "No"

def main():
    x = int(input("x: "))
    if pop(x):
        print("Yes")
    else:
        print("No")


def pop(n):
    return n % 3 == 0
     

main()
