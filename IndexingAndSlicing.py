import numpy as np

#Indexing and slicing - 
arr_index = np.array([1,2,3,4,5])
print(arr_index[: : 2]) #print 1 3 5



print("matrix")
matrix = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(matrix[0:2, 0: ]) # [row vaule:row value, column value:column value]
print(matrix[0:2,0:2]) # print 1 2 and 4 5

# Index array - Advance  Indexings
print("Advance Indexings")
arr_4 = np.array([1,2,3,4,5])
indx = (0,3)
print(np.take(arr_4,indx))

#Iteratings with nditer - 
arr5 = np.array([[1,2,3,
                 4,5,6]])

for i in np.nditer(arr5):
    print(i, end=" ")

# ndenumerate - both index + value
print("ndenemerate")
for indx, x in np.ndenumerate(arr5):
    print(indx,x)


#Transpose in matrix - 
print("Transpose of a matrix")
new_arr = np.array([[1,2],
                    [3,4]])
print(new_arr.transpose())

#SwapAxes - Swap 2 specific axes in a matrix
print("SwapAxes")
arr6 = np.array([[[1,2],[3,4]]])
print(arr6.shape)
swap_arr = np.swapaxes(arr6,0,1)
print("SwapAxes: ")
print(swap_arr.shape)

#Concatination
print("concatination - ")
a1 = np.array([1,2])
a2 = np.array([3,4])

combine = np.concatenate((a1,a2))
print(combine)
