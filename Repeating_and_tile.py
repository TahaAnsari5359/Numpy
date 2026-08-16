import numpy as np

#repeating
print("Repeating")
arr = np.array([1,2,3])
print(np.repeat(arr,2)) #(array, amount)

#tile - repeat the whole array 
print("tile")
print(np.tile(arr,2)) 
