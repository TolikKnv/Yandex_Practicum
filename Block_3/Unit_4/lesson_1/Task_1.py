# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
# Из модуля math импортируйте константу "пи".
from decimal import Decimal, getcontext
from math import pi

# Приведите константу "пи" к типу Decimal.
# Помните, что Decimal() принимает строку, а константа "пи" - это число.
PI = Decimal(str(pi))
# Установите необходимую точность для вычислений.
getcontext().prec = 10

# Объявите функцию find_ellipse_area() с двумя параметрами.
def find_ellipse_area(a,b):
    return PI*a*b

# Объявите три переменные типа Decimal -
# две длины полуосей эллипса и глубину пруда.
half_round_1 = Decimal('2.5')
half_round_2 = Decimal('1.75')
hight = Decimal('0.35')


# Вызовите функцию find_ellipse_area(), в аргументах передайте длины полуосей эллипса.
area = find_ellipse_area(half_round_1,half_round_2)

# Вычислите объём пруда: площадь * глубина.
V = area*hight

# Напечатайте фразы с результатами вычислений.
print(f'Площадь эллипса: {area} кв.м.')
print(f'Объём воды для наполнения пруда: {V} куб.м.')