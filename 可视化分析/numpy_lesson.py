import numpy as np
"""
创建一维函数
ndarray 多维数组
"""
arr1 = np.array([1,2,3])
# 这个array（【中间放的是列表，但都是数字】），内存空间相同
# 不同于列表，列表对存放的内容没有要求，内存空间不同
lst = [1, 2, 3, 4, 5]
print(lst, type(lst))
t1 = np.array([1,2,3])
print(t1)
print(type(t1))

# 创建二维数组
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
"""
numpy 会发生强制类型转换
str > float > int

数组的元素个数
一维数组：.size = n
二维数组：.size = m*n
"""
# 按照[]判断数组的维数
# 对数组进行计算可以直接 np.array*2
print(arr2.size)  # 6 = 2 * 3
print("__________________________")
"""
形状：
一维数组：.shape = (m,)有逗号，表示m列
二维数组：.shape = (n,m)表示n行，m列
三维数组：.shape = (n,m,p)n段 m行 p列
从大到小的[]进行判断
"""
arr3 = np.array([[[1,2],[1,3]],[[4,5],[6,7]]])
print(arr1.shape)
print(arr2.shape)
print(arr3)
print(arr3.shape)
print("________________________")
"""
.ndim 表示维度的问题
"""
print(arr3.ndim)
