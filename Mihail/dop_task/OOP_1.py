# class Container:
#     def __init__(self, name: str, volume: int, current_volume: int, pour_out: int = 100) -> None:
#         self.__name = name
#         self.__volume = volume
#         self.current_volume = current_volume
#         self.pour_out = pour_out
#
#     def pour_out_liquid(self) -> int:
#         if self.current_volume > 0:
#             self.current_volume -= self.pour_out
#             return self.pour_out
#         else:
#             print(f'{self.__name} пуст')
#             return 0
#
#     def pour_liquid(self, volume: int) -> None:
#         if self.current_volume + volume <= self.__volume:
#             self.current_volume += volume
#         else:
#             print(f'{self.__name} полон')
#
#     def info(self):
#         print(f'{self.__name} = {self.current_volume}')
#
# def main() -> None:
#     jug = Container(name='Jug', volume=1000, current_volume=1000)
#     glass = Container(name='Glass', volume=200, current_volume=0, pour_out=50)
#     i = 0
#     while i < 11:
#         jug.info()
#         glass.info()
#         glass.pour_liquid(jug.pour_out_liquid())
#         i += 1
#
# if __name__ == '__main__':
#     main()


class Purse:
    def __init__(self, valuta, name='Unknoun'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany


    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Недостаточно средств')
            raise ValueError ('Недостаточно средств')
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        print(self.__money)

    def __del__(self):
        print('Кошелёк удалён')



x = Purse('USD')
y = Purse("USD", 'Bill')
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()