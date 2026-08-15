import numpy as np
#arithmetic Operations
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1+arr2)

print(arr1-arr2)

print(arr1/arr2) # single (/) for normal devision

print(arr1*arr2)
print(arr2//arr1)  #for integer devision use (//)
print(arr2%arr1)  #Modulus For getting Remainder (%)
print(arr1**3)  #Exponential (power) Used For squaring and cube

#Universal Functions
arr3 = np.array([1,4,9,16])
print(np.sqrt(arr3)) #For square root

print(np.exp(arr3)) #FOr exponential

angles = np.array([0,np.pi,np.pi/2])
print(np.sin(angles)) #Sin FUnc
