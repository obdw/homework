'''Дан произвольный список, содержащий только числа.
Выведите результат сложения всех чисел больше 10.'''
numbers = [23, 3, 5, 55, 6, 12]
i = 0
sum = 0
while i < len(numbers):
    if numbers[i] > 10:
        sum += numbers[i]
    i += 1
print(sum)






