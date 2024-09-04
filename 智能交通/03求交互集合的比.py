while True:
    number = input()
    if number == "Q":
        break
    else:
        address_one = input()
        address_two = input()
        result_one = list(map(float, address_one.split(',')))
        # 这一步非常重要，是将字符串转化为数字列表
        result_two = list(map(float, address_two.split(',')))

        x1,y1,x2,y2 = result_one
        x3,y3,x4,y4 = result_two
        x_min = max(x1,x3)
        x_max = min(x2,x4)
        y_min = max(y1,y3)
        y_max = min(y2,y4)

        width = max(0,x_max-x_min)
        height = max(0,y_max-y_min)

        S1 = (x2-x1)*(y2-y1)
        S2 = (x4-x3)*(y4-y3)
        if width == 0 or height == 0:
            print("0")
        else:
         print("{:.2f}".format((width*height)/(S1 + S2 - width*height)))