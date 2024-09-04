def find_gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input())
num2 = int(input())

print(find_gcd(num1,num2))
