def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            i += 1
            return False
    return True

number = int(input())

print(check_prime(number))