import numpy as np

# dtypes in numpy -
# int32 and int64
# float32 and float64
# bool
# complex
# str


arr1 = np.array([1,25,3,5])
print(arr1.dtype) #Used to check Data Type


arr2 = np.array([1.5,2.5,3.5,4.5], dtype=int) #dtype is float we will convert to int
print(arr2) # removed decimal

#Type Casting - 

arr3 = np.array([1,2,3,4,5,6,7,8,9])
new_arr = arr3.astype(np.float64) #astype used for converting to another dtype
print(new_arr)

#another eg - 
arr4 = np.array([1.1,2.2,3.3,4.4])
new_arr4 = arr4.astype(np.int64)
print(new_arr4)

#type Casting Errors - 

arr5 = np.array(["1","2","hello"]) #it will raise error bcz 1 and 2 element is int but last one is str
new_arr5 = arr5.astype(np.int64)
print(new_arr5)


# creating multideminesional array
arr6 = np.array([[1,2,3,4,5],
         [5,6,7,8,5]])
print(arr6)
print(arr6.ndim)
print(arr6.shape)
print(arr6.size)
print(arr6.itemsize)
