import numpy as np

#Vectorization
arr = np.array([12,45,67,44,55])
def square(x):
    return x*x

vfunc = np.vectorize(square)
print(vfunc(arr))

#dealing with missing value
#np.nan - not a number
# np.inf and -np.inf - positive and negative infinitess

#np.isnan
#np.isinf
#np.isinfinite


a = np.array([1,2,3,np.nan,np.inf]) #np.nan means not a number
print(a)

print(np.isnan(a))
print(np.isinf(a))


