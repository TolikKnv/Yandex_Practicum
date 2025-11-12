class Product:
    # Опишите инициализатор класса и метод get_info()
    def __init__(self, name, kol):
        self.name = name
        self.kol = kol

    def get_info(self):
        return f"{self.name} (в наличии: {self.kol})"


class Kettlebell(Product):
    # Опишите инициализитор класса и метод get_weight()
    def __init__(self, name, kol, weight):
        super().__init__(name, kol)
        self.weight = weight

    def get_weight(self):
        return f"{self.get_info()}. Вес: {self.weight} кг"


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    def __init__(self, name, kol, size):
        super().__init__(name, kol)
        self.size = size

    def get_size(self):
        return f'{self.get_info()}. Размер: {self.size}'



# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
