def func(a,b):
    return a+b
print(func(1,2))

funca = lambda a,b:a+b
print(funca(1,2))

funcb = lambda x:[x[0],x[2]]
print(funcb("abcde"))

a = 4
b = 3
print(a) if a>b else print(b)

funcc = lambda x,y:x if x>y else y

a = lambda x:x**2
print(a(10))
