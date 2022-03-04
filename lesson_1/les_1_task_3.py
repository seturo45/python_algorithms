"""
По введенным пользователем координатам двух точек вывести уравнение
прямой вида y=kx+b, проходящей через эти точки
"""

print('Координаты первой точки')
x1 = float(input('Введите х1: '))
y1 = float(input('Введите y1: '))

print('Координаты второй точки')
x2 = float(input('Введите х2: '))
y2 = float(input('Введите y2: '))

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')
