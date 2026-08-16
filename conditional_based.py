import numpy as np

arr = np.array([10,20,30,40])
#where
print("where condition")
print(np.where(arr<3, "low", "high")) # (condition, "print", "else print")

#argwhere
print("argwhere")
print(np.argwhere(arr>0))

#logical and
print("logical and")
print(np.logical_and(arr>10, arr<30))


arr_matrix = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]])

print(np.argwhere(arr_matrix>5))

#advanced conditional using logical AND and logical OR
arr = np.array([10,20,30,40,80])
print("logical and")
print(np.logical_and(arr>20, arr<40))


print("logical OR")
print(np.logical_or(arr<20, arr<40))

#non zero
print("nonzeros")
arr1 = np.array([1,2,0,0])
print(np.nonzero(arr1))

