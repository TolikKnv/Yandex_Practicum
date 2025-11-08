# Количество корзин с овощами, шт.
baskets = 462
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175


# Допишите функцию, которая рассчитывает вес и стоимость урожая.
def calc(baskets, av_weight, price_per_kg):
    return baskets * average_weight, baskets * av_weight * price_per_kg


# Вызовите функцию calc() и обработайте вернувшееся значение.
total_weight, result = calc(baskets, average_weight, price_per_kg)
# Составьте f-строку и напечатайте её.
print(f"Общий вес урожая: {total_weight} кг. Оценённая стоимость урожая: {result}.")
