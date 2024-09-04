def find_even_numbers(num):
    list_one = []
    if num <= 1:
        return list_one
    else:
        return [i for i in range(1,num+1) if i % 2 == 0]
# 列表的推导式，[元素 for 元素 in list/range if 判断元素]
num = int(input())

print(find_even_numbers(num))