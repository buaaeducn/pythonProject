def find_unique_number(num_list):
    num_count = {}   # 空字典

    # 统计数字出现次数
    for num in num_list:
        if num in num_count:    # 对字典的键值对进行11计数
            num_count[num] += 1
        else:
            num_count[num] = 1

    # 找出只出现一次的数字
    for num, count in num_count.items():
        if count == 1:
            return num

    return None  # 如果没有只出现一次的数字，则返回None

numbers =  list(map(int,input().split()))
print(find_unique_number(numbers))


