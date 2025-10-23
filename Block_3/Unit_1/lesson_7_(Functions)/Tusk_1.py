def get_rectangle_area(len_rectangle,width_rectangle):
    return len_rectangle*width_rectangle


def get_rectangle_perimeter(len_rectangle,width_rectangle):
    return 2*(len_rectangle+width_rectangle)

# Длина прямоугольника.
length = 5
# Ширина прямоугольника.
width = 10

print('Площадь:', get_rectangle_area(length,width))
print('Периметр:', get_rectangle_perimeter(length,width))