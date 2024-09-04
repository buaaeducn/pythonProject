sensitive_character = "你好"
test_sentence = input("请输入一句话")
for char in test_sentence:
    if char in sensitive_character:
        test_sentence = test_sentence.replace(char, "*")
print(test_sentence)
