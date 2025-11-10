class BacteriaProducer:
    # Допишите инициализатор класса
    def __init__(self, max_bacteria):
        self.max_number = max_bacteria
        self.now_number = 0

    # Допишите метод
    def create_new(self):
        if self.now_number == self.max_number:
            print("Нет места под новую бактерию")
        else:
            self.now_number += 1
            print(
                f"Добавлена одна бактерия. Количество бактерий в популяции: {self.now_number}"
            )

    # Допишите метод
    def remove_one(self):
        if self.now_number == 0:
            print("В популяции нет бактерий, удалять нечего")
        else:
            self.now_number -= 1
            print(
                f"Одна бактерия удалена. Количество бактерий в популяции: {self.now_number}"
            )


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
