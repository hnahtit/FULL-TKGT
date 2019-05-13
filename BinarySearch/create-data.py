import random
n = int(input("Nhap so luong sample: "))
numbers = random.sample(range(0, 100000), n)
numbers.sort()
with open('sample4.txt', 'w') as f:
    f.write(str(n))
    f.write("\n")
    for item in numbers:
        f.write("%d" % item)
        f.write(" ")
print(numbers)