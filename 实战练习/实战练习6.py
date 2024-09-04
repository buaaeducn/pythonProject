def find_all_factors(num):
    factor_list = []
    if num < 1:
        return []
    for i in range(1,num+1):
        if num % i == 0:
           factor_list.append(i)  #拿一个列表进行存储
    return factor_list
# 输入一个数字
num = int(input())

# 调用函数
print(find_all_factors(num))