#declare variables
arr = []

#read data from file
f = open('sample_for_sort.txt','r')
for val in f.read().split():
    arr.append(int(val))
f.close()

#QuickSort
def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if(arr[j]<pivot):
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)
def quickSort(arr,low,high):
    if(low<high):
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

print("Original array:")
print(arr)
quickSort(arr,0,len(arr)-1)
print("Array after sort:")
print(arr)