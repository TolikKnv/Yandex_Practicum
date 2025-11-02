# Функция для создания словаря информации об овощах

def create_vegetable_info(vegetables, varieties, yields):
    cort_1 = zip(varieties, yields)
    vegetable_info = dict(zip(vegetables, cort_1))
    return vegetable_info

# Тестовые данные:
vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
varieties = ['Красный куб', 'Аллигатор', 'Василёк', 'Тропический закат', 'Арктик']
yields = [6.5, 4.3, 2.8, 2.2, 3.5]

# Вызов функции:
print(create_vegetable_info(vegetables, varieties, yields))