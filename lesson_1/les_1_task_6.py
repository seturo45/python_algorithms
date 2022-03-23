"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

letters = 'abcdefghijklmnopqrstuvwxyz'

letter_index = int(input('Введите номер буквы: '))
letter = letters[letter_index - 1]
print('Буква под номером {} - это "{}"'.format(letter_index, letter))
