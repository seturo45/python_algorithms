"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они
стоят, и сколько между ними находится букв
"""

letters = 'abcdefghijklmnopqrstuvwxyz'

letter_range = input('Введите две буквы через пробел: ').split(' ')

let_1 = letters.index(letter_range[0]) + 1
let_2 = letters.index(letter_range[1]) + 1

length = let_2 - let_1

print('Первая буква: {} - находится на {} позиции,\
      вторая буква {} - находится на {} позиции.\
      Расстояние между ними {}'.format(letter_range[0], let_1, letter_range[1], let_2, length))
