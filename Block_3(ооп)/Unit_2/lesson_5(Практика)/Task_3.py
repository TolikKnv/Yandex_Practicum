class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, price):
        price = round(price * (1-(self.__discount / 100)), 2)
        return price

    def set_discount(self, new_discount):
        if new_discount > 80:
            self.__discount = 80
        else:
            self.__discount = new_discount


customer = Customer("Иван Иванович")
customer.get_price(100)
customer.set_discount(20)
customer.get_price(100)
