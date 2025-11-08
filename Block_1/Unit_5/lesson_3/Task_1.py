def assess_yield(number_of_plants, average_weight):
    # Ваш код здесь
    total = number_of_plants * average_weight / 1000
    if total > 100:
        return total, "Ожидается отличный урожай."
    if total > 50:
        return total, "Ожидается хороший урожай."
    if total > 0:
        return total, "Урожай будет так себе."
    else:
        return total, "Урожая не будет."


# Пример вызова функции
total_weight, rating = assess_yield(50, 200)
print(total_weight, "кг.", rating)
