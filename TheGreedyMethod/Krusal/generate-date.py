import random
import numpy as np
n = int(input("Nhap so luong sample: "))
numbers = random.sample(range(1, 20), n)
arr = [[0 for x in range(n)] for y in range(n)]
# print(arr)
arr = np.random.randint(1,10,size=(n,n))
for i in range(n):
    for j in range(n):
        arr[j][i] = arr[i][j]
        arr[i][i] = 0
print(arr)

with open('data.txt', 'w') as f:
    f.write(str(n))
    for i in range(n):
        f.write("\n")
        for j in range(n):
            f.write("%d" % arr[i][j])
            f.write(" ")