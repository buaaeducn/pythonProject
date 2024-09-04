test_sentence = input("Enter a sentence: ")
result_sentence = test_sentence.upper()
count = 0
for i in range(len(test_sentence)):
    if test_sentence[i] != result_sentence[i]:
        count += 1
print(count)
