#declare variables
arr = []
min = 0
max = 0
min1 = 0
max1 = 0
min2 = 0
max2 = 0
#read data from file
f = open('sample_for_sort1.txt','r')
for val in f.read().split():
    arr.append(int(val))
f.close()

print(arr)
#solve function
def MinMax(arr,l,r):

    if(l == r):
        max = arr[l]
        min = arr[l]
    else:
        min1,max1= MinMax(arr,l,(l+r)//2)
        min2,max2= MinMax(arr, (l+r)//2+1,r)
        if(min1<min2):
            min = min1
        else:
            min = min2
        if(max1>max2):
            max = max1
        else:
            max = max2
    return min,max

min,max = MinMax(arr,0,len(arr)-1)
print(min)
print(max)