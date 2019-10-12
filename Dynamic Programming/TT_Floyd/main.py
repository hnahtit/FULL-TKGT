import numpy as np
import sys
from itertools import product
#read data from file
theFile = open('data.txt','r')
temp = []
#n la so phan tu cua mang
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
print(arr)
#Floyd
def FLoyd(a,n):
    vc = sys.maxsize
    d = [[0 for x in range(n)] for x in range(n)]
    p = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            d[i][j] = a[i][j]
            p[i][j] = 0
    for k in range(n):
        for i in range(n):
            if(d[i][k] > 0 and d[i][k]<vc):
                for j in range(n):
                    if(d[k][j] > 0 and d[k][j]< vc):
                        if(d[i][k] + d[k][j] < d[i][j]):
                            d[i][j] = d[i][k] + d[k][j]
                            p[i][j] = k
    return d,p

def FindReverse(T,u,v):
    i = T[u][v]
    if(i == 0):
        print(u)
    else:
        FindReverse(T,i,v)
        FindReverse(T,u,i)
def PrintReverse(T,u,v):
    if(T[u][v] == -1):
        return
    else:
        print(v)
        print("->")
        FindReverse(T,u,v)

d,p = FLoyd(arr,n)
for row in d:
    print(row)
for row in p:
    print(row)
PrintReverse(p,0,3)