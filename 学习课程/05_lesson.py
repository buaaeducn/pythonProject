lst = ["赵敏","张韶钢","赵本山","张无极"]

for i in range(0,len(lst)):
    item = lst[i]
    if item.startswith("张"):
        new_name = "王" + item[1:]
        lst[i] = new_name
print(lst)
