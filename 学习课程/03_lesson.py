name = input("Enter your name: ")
address = input("Enter your address: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

s = f"我叫{name},我住在{address},我今年{age}岁"
print(s)

verity_code = "xAd1"
user_input = input(f"请输入验证码{verity_code}")
if verity_code.upper() == user_input.upper():
    print("True")
else:
    print("False")
