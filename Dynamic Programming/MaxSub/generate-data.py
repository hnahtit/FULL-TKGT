import random
n = int(input("Nhap so luong sample: "))
numbers = random.sample(range(-10, 10), n)
#numbers.sort()
with open('data1.txt', 'w') as f:
    for item in numbers:
        f.write("%d" % item)
        f.write(" ")
print(numbers)