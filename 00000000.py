'''Вычислить квадратное уравнение ax 2 + bx + c = 0 (*)
D = b 2 – 4ac;
x 1,2 = (-b +/- sqrt (D)) / 2a
Предусмотреть 3 варианта:
1) Два действительных корня
2) Один действительный корень
3) Нет действительных корней'''
import math
a = int(input('Введите а '))
b = int(input('Введите b '))
c = int(input('Введите c '))
d = b**2 - 4 * a * c
print(d)
if d > 0:
    x_1 = (-b + math.sqrt(d)) / 2 * a
    x_2 = (-b - math.sqrt(d)) / 2 * a
    print(x_1, x_2)
elif d == 0:
    x_1 = (-b / 2 *a)
    print(x_1)
else:
    print('Нет действительных корней')
