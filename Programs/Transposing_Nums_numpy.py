import numpy as np
print("Transpose a 3D array")
n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))
n4 = int(input("Enter Number 4: "))
n5 = int(input("Enter Number 5: "))
n6 = int(input("Enter Number 6: "))
n7 = int(input("Enter Number 7: "))
n8 = int(input("Enter Number 8: "))
n9 = int(input("Enter Number 9: "))

arr = np.array([[n1,n2,n3],
               [n4,n5,n6],
               [n7,n8,n9]])

print("Before Transpose: ")
print(arr)
print("After Transpose: ")
print(arr.transpose())




