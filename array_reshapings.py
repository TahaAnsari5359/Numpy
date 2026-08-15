import numpy as np

#Array Reshaping
print("1d array - ")
arr = np.array([1,2,3,4,5,6,7,8])
print(arr)
print("reshaped array in format 2 row and 4 column")
reshaped = arr.reshape(2,4)
print(reshaped)
print("another reshaped array in format 4 row and 2 column")
ant_reshape = reshaped.reshape(4,2)

print(ant_reshape)

#Ravel - conver a array to 1d
print("converting (4,2) array in 1d ")
ravel_arr = ant_reshape.ravel()
print(ravel_arr)

#flatten
flaten_arr = ant_reshape.flatten()
print("flatten - ")
print(flaten_arr)




