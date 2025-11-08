# Код этой функции не меняйте.
def count_tiles(depth, length, width=None):
    if width is None:
        width = length

    width_side = 2 * width * depth
    length_side = 2 * length * depth
    bottom_tiles = length * width
    total = width_side + length_side + bottom_tiles

    return total


# Передайте в функцию нужный параметр и напишите её код.
def make_phrase(total):
    if total in range(11, 15):
        return f"{total} плиток"
    elif total % 10 == 1:
        return f"{total} плитку"
    elif total % 10 in range(2, 5):
        return f"{total} плитки"
    else:
        return f"{total} плиток"


total_tiles = count_tiles(2, 2, 2)
# Выведите на экран нужное сообщение.
print(f"Для строительства бассейна нужно заготовить {make_phrase(total_tiles)}")
