# Импортировать функцию для получения случайного значения
# и присвоить ей псевдоним rnd
from random import randint as rnd


# Объявить функцию get_dumplings_recommendation(),
# которая вернёт (return) случайное число в диапазоне от 10 до 20.
def get_dumplings_recommendation():
    print(f"Оптимальным количеством пельменей на сегодня будет {rnd(10, 20)}")


# Вызвать функцию get_dumplings_recommendation() и напечатать заданную фразу.
get_dumplings_recommendation()
