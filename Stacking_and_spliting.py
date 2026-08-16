import numpy as np

#STacks 
print("Stackings")
stack1 = np.array([[1,2],[3,4]])
stack2 = np.array([[5,6],[7,8]])
print("vstack")
print(np.vstack((stack1,stack2)))

print("hstack")
print(np.hstack((stack1,stack2)))

print("normal stack")
print(np.stack((stack1,stack2),axis=0)) # for 0 = row and 1 for column


#spliting 
print("spliting")
split_arr = np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.split(split_arr,2)) #(array, parts)

print("hsplit")
print(np.hsplit(split_arr,2)) #horizontal split
print("vsplit")
print(np.vsplit(split_arr,2)) # vertical
