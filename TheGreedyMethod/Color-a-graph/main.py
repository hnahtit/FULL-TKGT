import numpy as np
#read data from file
#read data from file

theFile = open('data.txt','r')
temp = []
#n la so phan tu cua mang mau
n = int(theFile.readline().format())
for val in theFile.read().split():
    temp.append(int(val))
theFile.close()

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


available = [True for i in range(n)]
vertex = [0 for i in range(n)]

def CorlorGraph():
    #khoi tao dinh dau tien duoc to mau dau tien
    vertex[0] = 0

    #khoi tao cac dinh con lai chua duoc to mau
    for i in range(1,n):
        vertex[i] = -1

    #to mau cac dinh con lai
    for i in range(1,n):
        for j in (ke[i]):
            if(vertex[j] != -1):
                available[vertex[j]] = False

        crz = 0
        for k in range(n):
            if (available[k] == True):
                break
            crz = crz + 1
        vertex[i] = crz
        for j in (ke[i]):
            if (vertex[j] != -1):
                available[vertex[j]] = True
for i in range(n):
    print("ke",i,"-",ke[i])
CorlorGraph()
print("Cac dinh da duoc to mau: ")
for i in range(n):
    print(i,vertex[i])

