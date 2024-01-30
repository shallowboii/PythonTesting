import numpy as np
a = np.array([1,2,3],dtype="int16")
print(a)
print(a.ndim) # Gives back the dimension of the array
b= np.array([[9.9,8.2,4.8],[2.3,1.6,6.5]])

print(b)
print(b.shape) # shape like its a 2x3 (2 rows, 3 columns)
print(a.dtype) # datatype like int16 int32
print(a.size) #how many items in this
print(a.itemsize) # how many byte for example : int16 = 2 bytes,int32 = 4 bytes  

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
result = c[1,5] # works just like in c#

print(result)
print(c[0, :]) #gives back the whole first row

print(c[0,1:-1:2]) #gives back the first row till the last by 2 steps

#Matrixes

zero = np.zeros((2,3))
print(zero)
ones = np.ones((4,3))
print(ones)
full = np.full((2,2),15)
print(full)

#Random
print(np.random.rand(4,2)) #Random numbers between 0 and 1 4 rows 2 columns
print(np.random.randint(-3,7,size=(3,3))) # random number between -3 and 7, in the size of an 3x3 matrix
print(np.identity(3)) #identity matrix one parameter because its a square