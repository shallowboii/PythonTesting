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

array = np.array([[1,2,3],[1,2,3]])
r1 = np.repeat(array,3,axis=1) #Repeats an array 
print(r1)
print()
print("Task")
print("------------------------")
print()
output = np.ones((5,5))
output[1:-1, 1:-1] = 0
output[2,2] = 9
print(output)

print()
print("------------------------")
print()

#Be careful of copying arrays
# for example
array1 = np.array([1,2,3])
array2 = array1.copy() #if you  want to copy it use the copy function
array2[0] = 100 # now the array1 and the b refferences the same array in the memory
print(array1)
print(array2)
array1=array1+1 # you can do basic arithmetics
print(array1)
print(np.cos(array1))
print(array1)


print()
print("------------------------")
print()

#Linear Algebra


lineararray1 = np.ones((2,3))
print(lineararray1)

lineararray2 = np.full((3,2),2) #matrix multiplication
print(lineararray2)

lineararray_result = np.matmul(lineararray1,lineararray2)
print(lineararray_result)

            #Determinant
lineararray3 = np.identity(3)
print(np.linalg.det(lineararray3))

#Statistics

stat  = np.array([[1,2,3],[4,5,6]])
print(np.min(stat,axis=1)) #gives back the min of the first and second row
#min, max, sum

#Reorganizing Arrays
before = np.array([[1,2,3,4],[5,6,7,8]]) #its a 2 by 4 lets make this into a 4 by 2 or a 1 by 8

after = np.reshape(before,(4,2))
#or
after = before.reshape((8,1))
print(after)

#Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

v3 = np.vstack([v1,v2,v2])
print(v3)
#the same for horizontal stacks

