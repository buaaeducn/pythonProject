def reverse_sentence_words(sentence):
    # 此处写你的代码
    list1 = sentence.split()
    # 生成单词列表
    reversed_list1 = list1[::-1]
    # 翻转，颠倒
    return ' '.join(reversed_list1)
    # 以空格为结尾

# 获取输入
sentence = input()
# 调用函数并打印结果
print(reverse_sentence_words(sentence))