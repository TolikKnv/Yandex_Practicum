def fibonacci(n):
    # Допишите функцию.
    num_1 = 0
    num_2 = 1
    k = 2
    yield num_1
    yield num_2
    while k != n:
        num_1, num_2 = num_2, num_1 + num_2
        yield num_2
        k += 1


sequence = fibonacci(10)
for number in sequence:
    print(number)
