def get_sorted_keys_values(dict_obj):
    # 此处写你的代码
    return sorted(dict_obj.keys()), dict_obj.values()
# 获取用户输入转为字典
dictionary = eval(input())

# 调用函数
print(get_sorted_keys_values(dictionary))