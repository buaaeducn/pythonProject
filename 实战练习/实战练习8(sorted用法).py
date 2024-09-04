def are_anagrams(string1, string2):
    str1 = string1.replace(" ","").upper()
    str2 = string2.replace(" ","").upper()

    if len(str1) != len(str2):
        return False

    sorted_string1 = sorted(str1)
    sorted_string2 = sorted(str2)

    if sorted_string1 == sorted_string2:
        return True
    else:
        return False

# 获取输入string1 和 string2
string1 = input()
string2 = input()
# 调用函数并打印结果
print(are_anagrams(string1, string2))