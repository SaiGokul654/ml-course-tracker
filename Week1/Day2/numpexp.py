import numpy as np
arr=np.array([1,2,3,4])
print(arr)

mean=np.mean(arr)
print(mean)

rearr=arr.reshape(4,1)
print(rearr)

max=np.max(arr)
print(max)

matrix=np.array([[1,2],[3,6]])
transpose=np.transpose(matrix)
print(transpose)


seq=np.arange(0,10,2)
print(seq)

arr2=np.array([4,8,4,0,2,5,7,8])
sort=np.sort(arr2)
print(sort)

uni=np.unique(arr2)
print(uni)