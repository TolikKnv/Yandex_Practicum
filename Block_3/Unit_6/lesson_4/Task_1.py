fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.
# Объявляем новый список, в него будем складывать изменённые значения.
corrected_fruit_yields = []

# Объявите цикл, в нём переберите список fruit_yields.
# В теле цикла к каждому значению списка добавьте 1.2,
# затем получившееся значение сохраните в список corrected_fruit_yields.
for fruit_weight in fruit_yields:
    fruit_weight += 1.2
    corrected_fruit_yields.append(fruit_weight)
# Чтобы увидеть, что получилось,
# напечатаем список с откорректированными значениями.
print(corrected_fruit_yields)
