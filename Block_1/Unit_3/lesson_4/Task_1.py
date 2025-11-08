# Вместо многоточия укажите необходимые параметры.
def count_tiles(depth, length, width=0):
    # Опишите условие, когда ширина бассейна не указана.
    if width == 0:
        return length**2 + 4 * (depth * length)

    # Посчитайте, сколько понадобится плиток для стенок и дна бассейна.
    else:
        # Верните результат работы функции.
        return length * width + 2 * (depth * (length + width))


total_tiles = count_tiles(2, 2, 2)
print("Общее количество плиток для строительства бассейна:", total_tiles)
