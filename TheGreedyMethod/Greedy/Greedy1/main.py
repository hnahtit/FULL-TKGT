
# weight - value
value = []
weight =[]
#read data from file
theFile = open('Greedy.txt','r')
n = theFile.readline().format()
for val in theFile.readline().split():
    weight.append(int(val))
for val in theFile.readline().split():
    value.append(int(val))
theFile.close()

b = int(input("Nhap trong luong cua tui: "))

for i in range(n):


print(weight)
print(value)
print(b)
