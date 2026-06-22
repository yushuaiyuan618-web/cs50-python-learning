# Exercise 2: Function Practice (return)

# 目标：
# 1. 定义函数 cube(n)
# 2. 返回 n 的立方 (n³)
# 3. 在 main 中调用函数
# 4. 输出结果

# 示例：
# n: 3
# output: cube is 27

# TODO:
# 1. define function cube(n)
# 2. return n * n * n
# 3. define main()
# 4. input number
# 5. call function
# 6. print result

# 最后调用 main()

def cube(n):
    return(n*n*n)

def main():
    n = float(input("n: "))
    print(f"cube is {cube(n)}")

main()
