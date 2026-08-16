import numpy as np

arr = np.array([1,2,3])

print("sum")
print(np.sum(arr))

print("mean")
print(np.mean(arr))

print("median")
print(np.median(arr))

print("Standard Deviation")
print(np.std(arr))

print("variants")
print(np.var(arr))

print("min value")
print(np.min(arr))

print("max")
print(np.max(arr))

#eg
arr_matrix = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]])

print("sum in matrix")
print(np.sum(arr_matrix,axis=0)) # 0 = column 1 = row

#cumulative operations - 
print("cumilative sum")
print(np.cumsum(arr)) #1st elments , 1+2 elements, 1+2+3 elements

print("sumilative product")
print(np.cumprod(arr))
