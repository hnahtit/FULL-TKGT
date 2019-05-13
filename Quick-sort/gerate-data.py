import random
n = int(input("Nhap so luong sample: "))
numbers = random.sample(range(0, 10000), n)
#numbers.sort()
with open('sample_for_sort.txt', 'w') as f:
    for item in numbers:
        f.write("%d" % item)
        f.write(" ")
print(numbers)