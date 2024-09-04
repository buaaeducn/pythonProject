lst = ["赵敏","张韶钢","张无忌","五组天","嬴政","马超"]

temp = []
# 准备一个临时列表，负责储存要删除的内容
for item in lst:
    if item.startswith("张"):
        temp.append(item)
        # 将要删除的内容记录下来

for i in temp:
    lst.remove(i)
print(lst)