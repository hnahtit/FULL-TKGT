# read data from file
theFile = open('data.txt','r')
str1 = theFile.readline().replace('\n','')
str2 = theFile.readline().replace('\n','')
theFile.close()

def LCS(x,y,m,n):
    # cot - hang
    #m dai string 1
    #n dai string 2
    K = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(1,m + 1):
        t = 0
        for j in range(1,n + 1):
            if x[i - 1] == y[j - 1]:
                K[i][j] = K[i - 1][j - 1] + 1
            else:
                K[i][j] = max(K[i - 1][j], K[i][j - 1])
    return K[m][n],K

m = len(str1)
n = len(str2)
a,K = LCS(str1,str2,m,n)

S = []
i = m
j = n
while(i>0):
        if(K[i][j] - 1 ==  K[i-1][j-1]):
            S.append(str1[i-1])
            i = i - 1
            j = j -1
        else:
            i = i - 1
            j = j -1

S = S[::-1]
for row in K:
    print(row)
# print(K)
print(S)
print(a)


