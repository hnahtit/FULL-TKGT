import random
n = int(input("Nhap so luong sample: "))
numbers = random.sample(range(1, 20), n)
value = random.sample(range(1, 20), n)
#numbers.sort()
with open('Greedy.txt', 'w') as f:
    f.write(str(n))
    f.write("\n")
    for item in numbers:
        f.write("%d" % item)
        f.write(" ")
    f.write("\n")
    for item in value:
        f.write("%d" % item)
        f.write(" ")