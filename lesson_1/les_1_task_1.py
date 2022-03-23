"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
number = input('Введите трехзначное число: ')

summ = 0
prod = 1

for i in number:
    summ += int(i)
    prod *= int(i)
print(f'Сумма: {summ}')
print(f'Произведение: {prod}')
