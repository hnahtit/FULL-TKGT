import numpy as np
#read data from file
#read data from file
theFile = open('data.txt','r')
temp = []
n = int(theFile.readline().format())
for val in theFile.read().split():
    temp.append(int(val))
theFile.close()

print(temp)

arr = np.random.rand(n,n)
k = 0
for i in range(n):
    for j in range(n):
        arr[i,j] = temp[k]
        k = k+1
print(arr)