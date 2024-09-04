print("Hello World")
# 单行注释
"""

# 变量的基础类型
a = input("请输入第一个数字：")
b = input("请输入第二个数字：")
print(type(a))
a = int(a)
b = int(b)
print(type(a))
print(a+b)
"""

# 第二种if
money = input("请输入钱：")
money = int(money)
if money > 1000:
    print("做足疗")
    if money > 5000:
        print("充个会员卡")
    else:
        print("洗个脚就走")
else:
    print("回家")
print(789)

# _______第四种if_________#
if money > 5000:
    print(123)
elif money > 1000:
    print(456)
else:
    print(123)

i = 1
while i <= 100:
    print(i)
    i += 1
    if i == 10:
        continue
