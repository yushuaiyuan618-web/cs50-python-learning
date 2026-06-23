# Exercise 6: Login Checker

# 目标：
# 预设用户名 = "admin"
# 预设密码 = "1234"

# 输入 username + password

# 输出：
# 正确 → "Login successful"
# 错误 → "Login failed"

username = "admin"
passward = "1234"

input_username = input("Username: ")
input_passward = input("Passward: ")
if input_username == username and input_passward == passward:
    print("Login successful")
else:
    print("Login failed")