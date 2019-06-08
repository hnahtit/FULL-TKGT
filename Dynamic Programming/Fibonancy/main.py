def Fibo(n):
    arr = [0 for i in range(10000)]
    arr[0] = 0
    arr[1] = 1
    if(n > 1):
        for i in range(2,n):
            arr[i] = arr[i-1]+ arr[i-2]
    return arr[n]

print(Fibo(5))