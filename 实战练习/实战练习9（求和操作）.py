def is_project_divisible_by_sum(number_list):
    total_sum = 0
    total_product = 1

    for num in number_list:
        total_sum += num
        total_product *= num

    return total_product % total_sum == 0


# 输入整数列表并转换为列表
number_list = list(map(int, input().split()))

# 调用函数并打印结果
print(is_project_divisible_by_sum(number_list))

