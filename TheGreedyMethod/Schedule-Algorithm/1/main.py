from collections import OrderedDict
thisdict =	{
  "1" : (6,8),
  "2": (7,10),
  "3": (5, 11),
  "4": (13,14),
  "5": (9,16),
  "6": (12,18),
  "7":(17,20),
  "8":(15,19)
}
name = [0 for i in range(len(thisdict)-1)]
begin_val = [0 for i in range(len(thisdict)-1)]
end_val = [0 for i in range(len(thisdict)-1)]
mt = sorted(thisdict.items(), key = lambda x: x[1])

for i in range(len(thisdict)-1):
    name[i] = mt[i][0][0]
    begin_val[i] = mt[i][1][0]
    end_val[i] = mt[i][1][1]

print(name)
print(begin_val)
print(end_val)
S = [0 for i in range(len(thisdict)-1)]
u = 0
t = 0
k = 0
S[k] = name[t]

while(u<len(thisdict)-1):
    if(begin_val[u] < end_val[t]):
        u = u + 1
    elif(begin_val[u] > end_val[t]):
        k = k +1
        S[k] = name[u]
        t = u

print(S)

