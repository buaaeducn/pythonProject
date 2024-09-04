def max_min(list_nums):
    list_nums.sort()
    return list_nums[len(list_nums)-1] - list_nums[0]

numbers = list(map(int,input().split()))
print(max_min(numbers))
"""
这行代码 numbers = list(map(int, input().split())) 在 Python 中的作用是将用户输入的一行数字字符串分割成单个数字，并将其存储在一个整数列表中。
让我们逐步解释这行代码的功能：
input() 函数用于从标准输入（通常是键盘输入）读取一行输入，并返回一个字符串。
split() 方法被调用在这个输入字符串上，没有传递参数时，默认按照空格分割字符串。它将这行输入字符串分割成一个由多个子字符串组成的列表。
map(int, ...) 是 Python 内置函数 map() 的用法。它将 int 函数应用于 split() 方法返回的列表中的每个元素，将每个子字符串转换为整数。
list(...) 将 map 函数返回的结果转换为一个列表。因此，最终的 numbers 列表包含了用户输入的每个整数。
"""