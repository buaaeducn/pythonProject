def is_string_isogram(word):
    # 将单词转换为小写
    word = word.lower()
    # 在此处编写你的代码
    count = {}
    for letter in word:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1

    for i in count:
        if count[i] > 1:
            return False
    return True
"""
不区分大小写，可以先将单词转换为小写。
可以使用for循环遍历单词中的每个字母，然后使用count()函数来计算字母在单词中出现的次数。
"""
# 从用户处获取输入
word = input()
# 调用函数
print(is_string_isogram(word))