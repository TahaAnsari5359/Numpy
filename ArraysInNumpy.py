import numpy as np

# 1 dimension array
arr1 = np.array([2])  
print(arr1.ndim)

# 3 dimens Array depend on Brackets 
arr2 = np.array([[[]]])
print(arr2.ndim)


# Arrange In NP
ranges = np.arange(1,10,2) #(start, stop, step)
print(ranges)

#linspace 
lin_space = np.linspace(0,1,4) #(start, stop, num of value betw them)
print(lin_space)

#logartihmic Scale Array
log_spa =  np.logspace(1,2,3) #(starting power value, Ending power value, No of value)
print(log_spa)

#Zeros
zero_arr = np.zeros(5)
print(zero_arr)

more_zero = np.zeros([2,3,4,5])
print(more_zero)

#Ones
ones_arr = np.ones([4,2]) #[row,column]
print(ones_arr)

#full
our_choice = np.full(10,2) #10 elements, default value 2
print(our_choice)

fulls = np.full([10,5],7.5) #([row,column],default value)
print(fulls)

#unInitialized array
emptyy = np.empty([2,3])
print(emptyy)


# Random floats
randomss = np.random.rand(2,3) #row and column but not inside []
print(randomss)

randnn = np.random.randn(2,3) #Random floats from standard normal distribution
print(randnn)

random_int = np.random.randint(10,100) #random number from 10 to 100
print(random_int)
