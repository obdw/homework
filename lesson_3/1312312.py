'''Ввести почтовый адрес. Проверить доменное имя. В случае если оно
gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
“DOMAIN NAME is not'''
a = input('Введите e-mail: ')
b = 'gmail.com'
if b in a:
    print(a)
else:
    print('DOMAIN NAME is not supported')

