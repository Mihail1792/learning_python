from enum import Enum


class PizzaType(Enum):
    """
    Перечисление текущих рецептов пицц в пиццерии,
    которые можно приготовить
    """
    MARGARITA = 0,
    MEXICO = 1,
    STELLA = 2


class Pizza:
    """
    Базовый класс для пицц, которые можно
    приготовить в пиццерии
    """
    def __init__(self, price: float):
        self.__price = price # цена пиццы

    def get_price(self) -> float:
        return self.__price


class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(3.5)


class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(17.5)


class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(5.5)


def create_pizza(pizza_type: PizzaType) -> Pizza:
    """
    Factory Method
    """
    factory_dict = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.MEXICO: PizzaMexico,
        PizzaType.STELLA: PizzaStella
    }
    return factory_dict[pizza_type]()


if __name__ == '__main__':
    for pizza in PizzaType:
        my_pizza = create_pizza(pizza)
        print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')


class Product:
    def release(self):
        pass


class Car(Product):
    def release(self):
        print("Выпущен новый легковой автомобиль")


class Truck(Product):
    def release(self):
        print("Выпущен новый грузовой автомобиль")


class WorkShop:
    def create(self) -> Product:
        pass


class CarWorkShop(WorkShop):
    def create(self):
        return Car()


class TruckWorkShop(WorkShop):
    def create(self):
        return Truck()


if __name__ == "__main__":
    creator = CarWorkShop()
    car = creator.create()

    creator = TruckWorkShop()
    truck = creator.create()

    car.release()
    truck.release()


# https://www.youtube.com/watch?v=b87VdVrGQXc

