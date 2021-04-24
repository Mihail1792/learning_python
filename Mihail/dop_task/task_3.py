class Goods_at_the_shop:

    def __init__(self, variety: str, quantity: int, price: int, discount: float): #Наименование, количество, цена, скидка
        self.variety = variety
        self.quantity = quantity
        self.price = price
        self.discount = discount
        print("Приветствуем Вас в нашем гипермаркете!")


    def my_discount(self):
        result = round(self.price * self.discount * self.quantity, 2)
        print("Цена со скидкой:", result)

    def my_quantity(self):
        result = round(self.price * self.quantity, 2)
        print("Цена за ваши товары без скидки:", result)


    def print_info(self):
        print("Вами выбран товар:", self.variety, "В количестве:", self.quantity, "штук")

p1 = Goods_at_the_shop(variety="Телефон", quantity=2, price=99, discount=0.9)
p1.print_info()
p1.my_discount()
p1.my_quantity()

p2 = Goods_at_the_shop(variety="Телевизор", quantity=1, price=1000, discount=0.95)
p2.print_info()
p2.my_discount()
p2.my_quantity()


class Computer_accessories(Goods_at_the_shop):
    pass
p3 = Computer_accessories(variety="Клавиатура", quantity=1, price=600, discount=0.85)
p3.print_info()
p3.my_discount()
p3.my_quantity()


class Phones_accessories(Goods_at_the_shop):
    pass