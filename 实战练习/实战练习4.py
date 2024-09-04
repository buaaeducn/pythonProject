def list_between(start, end):
    return list(range(start+1, end))  # 生产一个从start+1到end-1的数字列表

start = int(input())
end = int(input())

print(list_between(start, end))