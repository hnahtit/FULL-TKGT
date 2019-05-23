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

def prim(c,n,start):
    passed = []
    cost = []
    passed.append(start)
    while 1:
        mincost = 99999
        node = -1
        for point in passed:
            for i in range(n):
                if i not in passed and c[point][i]>0:
                    if c[point][i] < mincost:
                        mincost = c[point][i]
                        node = i
        passed.append(node)
        cost.append(mincost)
        if len(passed) == n:
            break
    return cost,passed

if __name__ == '__main__':

    cost, passed = prim(arr, n, int(input("Nhap diem bat dau: ")))
    print('lowcost: {}'.format(cost))
    print('passed: {}'.format(passed))