# name - weight - value
name = []
weight =[]
value = []
#0385724398

#read data from file
theFile = open('data.txt','r')

n = int(theFile.readline().format()) # n la so do vat

for val in theFile.readline().split():
    name.append(val)
for val in theFile.readline().split():
    weight.append(int(val))
for val in theFile.readline().split():
    value.append(int(val))
theFile.close()

b = int(input("Nhap trong luong cua tui: "))


print("w = ",weight)
print("c = ",value)
print(name)
# print(b)

s = []
# def BagBest():
#     MaxV = [[0 for i in range(b + 1)] for j in range(n + 1)]
#     for i in range(n+1):
#         for l in range(b+1):
#             MaxV[i][l] = MaxV[i][l-1]
#             if(l > weight[i] and (MaxV[i-1][l - weight[i]]+value[i] > MaxV[i-1][l])):
#                 MaxV[i][l] = MaxV[i-1][l-weight[i]]+value[i]
#                 s.append(i)
#     return MaxV[n][b]

def knapSack(b, wt, val, n):
    K = [[0 for x in range(b + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for l in range(b + 1):
            if i == 0 or l == 0:
                K[i][l] = 0
            elif wt[i - 1] <= l:
                K[i][l] = max(val[i - 1] + K[i - 1][l - wt[i - 1]], K[i - 1][l])
            else:
                K[i][l] = K[i - 1][l]
                s.append(i)

    return K[n][b],K

a, MaxV = knapSack(b,weight,value,n)
# print(MaxV)
for row in MaxV:
    print(row)
