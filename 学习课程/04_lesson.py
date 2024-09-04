lst = []
# append()追加
lst.append("1")
lst.append("2")
lst.append("3")
# 1 2 3
# insert()插入
lst.insert(0,"4")
# 4 1 2 3
# extend()合并两个列表
lst.extend(["5","6","7"])
# 4 1 2 3 5 6 7
# 删除
ret = lst.pop(3)
# 4 1 2 5 6 7
lst.remove("6")
# 4 1 2 5 7
# 修改
lst[4] = "10"
# 4 1 2 5 10
print(lst)
