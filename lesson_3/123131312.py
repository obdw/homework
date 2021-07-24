a = int(input('Введите количество рублей: '))
b = int(input('Введите количество копеек: '))
if a >= 1 and b >= 1:
    print(f'{a} Рублей {b} копеек')
if a >= 1 and b == 0:
    print(f'{a} Рублей')
if a == 0 and b >= 1:
    print(f'{b} Копеек')
if a == 0 and b ==0:
    print('Нет средств')