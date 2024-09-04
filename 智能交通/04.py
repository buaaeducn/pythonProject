input_number = input()
result = list(map(int, input_number.split(',')))
# important issues
a1,b1,a2,b2 = result
if a1 == 0 and b1 ==0:
    if a2 == 0 and b2 ==0:
        print("不动")
    elif a2 == 0 and b2 == 1:
        print("-1")
    elif a2 == 1 and b2 == 0:
        print("+1")
    else:
        print("-2")
elif a1 == 0 and b1 ==1:
    if a2 == 0 and b2 ==0:
        print("+1")
    elif a2 == 0 and b2 == 1:
        print("不动")
    elif a2 == 1 and b2 == 0:
        print("+2")
    else:
        print("-1")
elif a1 == 1 and b1 ==0:
    if a2 == 0 and b2 ==0:
        print("-1")
    elif a2 == 0 and b2 == 1:
        print("+2")
    elif a2 == 1 and b2 == 0:
        print("不动")
    else:
        print("+1")
else:
    if a2 == 0 and b2 ==0:
        print("-2")
    elif a2 == 0 and b2 == 1:
        print("+1")
    elif a2 == 1 and b2 == 0:
        print("-1")
    else:
        print("不动")
