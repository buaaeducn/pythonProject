def ends_with(string1, string2):
    if string1.endswith(string2):  # endswith用法
        return True
    else:
        return False

string1 = input()
string2 = input()

print(ends_with(string1, string2))