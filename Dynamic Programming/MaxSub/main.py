import sys
#declare variables
arr = []

#read data from file
f = open('data.txt','r')
for val in f.read().split():
    arr.append(int(val))
f.close()

print("Mang da cho:", arr)
def MaxSubVector(a,n):
    maxS = a[1]
    maxE = a[1]
    for i in range(2,n):
        if(maxE>0):
            maxE = maxE + a[i]
        else:
            maxE = a[i]
            s1 = i
        if(maxE > maxS):
            maxS = maxE
            e = i
            s = s1
    return  maxS,s,e

maxSub, s, e = MaxSubVector(arr,len(arr))
print("Tong day con lon nhat:",maxSub,"\nChi so dau:", s,"- Chi so cuoi:" , e)