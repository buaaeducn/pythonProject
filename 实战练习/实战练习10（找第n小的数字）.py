def find_nth_smallest(numbers_list,n):
    numbers_list.sort()
    if n > len(numbers_list):
        return None
    else:
        return numbers_list[n-1]

numbers_list = list(map(int,input().split()))

n = int(input())

print(find_nth_smallest(numbers_list,n))