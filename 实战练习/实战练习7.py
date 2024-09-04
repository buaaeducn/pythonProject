def reverse_number_digits(num):
    factor_list = []
    while int(num) % 10 != 0:
        factor_list.append(int(num) % 10)
        num = int(num) / 10
    return factor_list
# 获取用户输入
num = int(input())

# 调用函数
print(reverse_number_digits(num))