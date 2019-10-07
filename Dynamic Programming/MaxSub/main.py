import sys
#declare variables
arr = []

#read data from file
f = open('data.txt','r')
for val in f.read().split():
    arr.append(int(val))
f.close()

print("Mang da cho:", arr)
# def MaxSubVector(a,n):
#     maxS = 0
#
#     maxE = a[0]
#     for i in range(1,n):
#         if(maxE>0):
#             maxE = maxE + a[i]
#         else:
#             maxE = a[i]
#             s1 = i
#         if(maxE > maxS):
#             maxS = maxE
#             e = i
#
#     return  maxS,s1,e
#tim tong day con lon nhat

def MaxSubVector(a, n):
    f = [[0 for x in range(n+1)] for x in range(2)]
    f[0][0] = a[0]
    f[1][0] = 0
    for i in range(1 , n+1):
        f[0][i] = max(f[0][i-1], f[1][i-1])
        f[1][i] = max(a[i-1] , a[i-1] + f[1][i-1]) # a[i-1] thuc chat la a[i]
    f[1][n] = max(f[0][n],f[1][n])

    S = []
    i = n
    while(i > 0):
        if(f[1][i]- a[i-1] == f[1][i-1]):
            S.append(i)
            i = i -1
        else:
            i = i -1

    return f[1][n],S
#truy vet

# maxSub, s, e = MaxSubVector(arr,len(arr))
maxSub,S = MaxSubVector(arr,len(arr))
print("Tong day con lon nhat:",maxSub,S)