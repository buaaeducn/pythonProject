def calc_tetrahedral_number(n):
    count = {}
    for i in range(1,n+1):
        count[i-1] = 2
num = int(input())
print(calc_tetrahedral_number(num))