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
weight.append(-1)
value.append(-1)

print("w = ",weight)
print("c = ",value)

def knapSack(b, weight, val, n):
    K = [[0 for x in range(b+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(b+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif w < weight[i]: #w :1->19
                #phuong an toi uu la chon phuong an toi uu cua thang ben tren no
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(K[i - 1][w], val[i] + K[i - 1][w - weight[i]])

    return K[n][b],K


for i in range(n,0,-1):
    weight[i] = weight[i-1]
    value[i] = value[i-1]

a, MaxV = knapSack(b,weight,value,n)

S = []
Sum = 0
w = b
i = n
while(w>1):
        if(MaxV[i][w]  - value[i] == MaxV[i-1][w-weight[i]]):
            S.append(i)
            Sum = Sum + weight[i]
            w = w - weight[i]
            i = i - 1
        else:
            i = i - 1


for row in MaxV:
    print(row)
print(Sum,'\n',S)