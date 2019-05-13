import random


def BinarySearch(arr, l, r, x):
    if r>=l:
        mid = l+(r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return BinarySearch(arr,l,mid-1,x)
        else:
            return BinarySearch(arr,mid +1,r,x)            
    else:
        return -1

#read data from file
theFile = open('sample3.txt','r')
arr = []
n = theFile.readline().format()
for val in theFile.read().split():
    arr.append(int(val))
theFile.close()
#print(arr)

#arr = [2,4,5,10,14,15]

x = int(input("Input value need search: "))
result = BinarySearch(arr,0, len(arr)-1,x)
if result != -1:
    print("element is {0}".format(result))
else:
    print("No element")

# #test
# for x in arr:
#     if x == 78580:
#         print(arr.index(x))