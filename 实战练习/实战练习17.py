def find_first_n_odds(num):
    lisr1 = []
    count = 0
    number = 1
    while count < num:
        if number % 2 == 0:
            number += 1
        else:
            lisr1.append(number)    # 对列表进行添加
            number = number + 1
            count += 1

    return lisr1
n = int(input())

print(find_first_n_odds(n))