decimal = 10
bin_num = 0b1010
print(bin(decimal))   # bin(x)转化为2进制
print(oct(decimal))   # oct(x)转化为8进制
print(hex(decimal))   # hex(x)转化为16进制


print("复数")
complex_one = 1 + 2j
# 复数 = real + imag j
print(complex_one.real)
print(complex_one.imag)   # 提取实部，和虚部

print("数字类型转换,注意格式")
num_one = 2
print(float(num_one))
print(complex(num_one))


# 运算符
# := 海象运算符，用于表达式内部赋值
# 逻辑运算符 and or not
# 成员运算符 in 给定数据是否在序列中  not in 给定数据不在序列中
x = "python"
y = 'p'
print(y in x)
