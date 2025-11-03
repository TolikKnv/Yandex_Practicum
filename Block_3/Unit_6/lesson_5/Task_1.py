# Пригодится для наполнения списков!
import random

# 1. Создание списка списков:
harvest = [
    [random.randint(5, 20) for i in range(3)] for j in range(3)
]  # Примените list comprehension.
print(harvest)

# 2. Функция для подсчёта общего урожая:
def total_harvest(harvest):
    sum = 0
    for i in harvest:
        for j in i:
            sum += j
    return sum


# 3. Функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(harvest):
    list = []
    for i in harvest:
        list.append(sum(i) / 3)
    return list


# Вывод результатов
print("Урожай с каждой грядки на каждом участке:", harvest)
print("Общий урожай со всех участков:", total_harvest(harvest))
print("Средний урожай с каждого участка:", average_harvest_per_plot(harvest))
