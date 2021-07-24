a = [12, 44, 67, 78, 53]
print(a)
for i in range(len(a)):
    a[i] *= -2
print(a)

b = 0
while b < len(a):
    a[b] *= -2
    b += 1
print(a)
