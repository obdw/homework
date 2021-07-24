'''Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0').'''


while True:
    sign = input("Знак (+,-,*,/): ")
    if sign == '0':
        break
    if sign in ('+', '-', '*', '/'):
        x = int(input("x="))
        y = int(input("y="))
        if sign == '+':
            print(x + y)
        elif sign == '-':
            print(x - y)
        elif sign == '*':
            print(x * y)
        elif sign == '/':
            if y != 0:
                print(x / y)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак !!!")

