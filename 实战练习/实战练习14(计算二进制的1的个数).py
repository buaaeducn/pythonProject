def count_binary_ones(num):
    return bin(num).count('1')

num = int(input())

print(count_binary_ones(num))
