import numpy as np
import random
#read data from file

theFile = open('data.txt','r')
temp = []
#n la so phan tu cua mang mau
n = int(theFile.readline().format())
for val in theFile.read().split():
    temp.append(int(val))
theFile.close()
# random_vertex = [random.randint(1,n-1) for i in range(n-1)]
# print(random_vertex)
random_vertex = [4,0,1,3,2]

# print(random_vertex)
arr = np.random.rand(n,n)
k = 0
for i in range(n):
    for j in range(n):
        arr[i,j] = temp[k]
        k = k+1
# print(arr)
#tao 1 mang de chua ma tran cac dinh ke
ke = []
for i in range(n):
    ke.append([])

#dua cac dinh vao mang ke
for i in range(n):
    for j in range(n):
        if(arr[i,j] == 1):
            ke[i].append(j)

available = [False for i in range(n)]
vertex = [0 for i in range(n)]

def CorlorGraph():
    # #khoi tao dinh dau tien duoc to mau dau tien
    vertex[random_vertex[0]] = 0

    #khoi tao cac dinh con lai chua duoc to mau
    for i in random_vertex[1:]:
        vertex[i] = -1

    #to mau cac dinh con lai
    for i in random_vertex[1:]:
        for j in (ke[i]):
            if(vertex[j] != -1):
                available[vertex[j]] = True

        crz = 0
        for k in range(n):
            if (available[k] == False):
                break
            crz = crz + 1
        vertex[i] = crz
        for j in (ke[i]):
            if (vertex[j] != -1):
                available[vertex[j]] = False
for i in range(n):
    print("ke",i,"-",ke[i])
CorlorGraph()
print("Cac dinh da duoc to mau: ")
for i in range(n):
    print(i,vertex[i])

