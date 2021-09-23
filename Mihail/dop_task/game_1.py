import random


class Game:
    """Словарь с колодой и номиналом карт"""
    playing_cards = {
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Валет": 2, "Дама": 3, "Король": 4, "Туз": 11
    }

    def __init__(self, name):
        self.name = name
        self._money = 1000
        print(f"\nДобрейший вечерочек, {self.name}")

    def info(self):
        print(f'Ваш баланс, {self.name}: {self.__money}$')

    """Метод, который рандомно выдаёт карты и показывает их номинал"""

    def get_card(self):
        player_card = random.choice(list(self.playing_cards.keys()))
        value = self.playing_cards.get(player_card)
        print(f'Ваша карта: {player_card}, Номинал: {value}')
        return value

    """Реализация ставки"""

    def bets(self):
        bet = 0
        bet += Player.top_down_balance(self, int(input(f'Укажите сумму ставки: ')))
        return bet

    """Метод, который пополняет кошелёк"""

    def top_up_balance(self, howmany):
        self._money = self.__money + howmany
        return howmany

    """Метод, который снимает деньги с кошелька"""

    def top_down_balance(self, bet):
        if self._money - bet < 0:
            print('Недостаточно средств')
            raise ValueError('Недостаточно средств')
        self._money = self._money - bet
        return bet


class Player(Game):
    """Метод, который считает сумму очков"""

    def get_result(self, value, bet):
        card_sum = 1
        value_sum = value
        while card_sum != 5:
            player_input = input(f'Нужно дабавить карту {self.name} y/n?: ')
            if player_input == 'y':
                card_sum += 1
                value_sum += Player.get_card(self)
                if value_sum > 21:
                    print('Перебор, вы проиграли')
                    break
                print(f'Сумма очков: {value_sum}\n')
            if player_input == 'n':
                break
        return print(f'Итоговая сумма очков: {value_sum}')


class Dealer(Player):

    def bets(self):
        bet = self._money
        print(f'Банк: {bet}')
        return bet

    def get_result(self, value, bet):
        card_sum = 1
        value_sum = value
        while card_sum != 5:
            player_input = input(f'Нужно дабавить карту {self.name} y/n?: ')
            if player_input == 'y':
                card_sum += 1
                value_sum += Dealer.get_card(self)
                if value_sum == 17:
                    break
                elif value_sum > 21:
                    print('Перебор, банкир проиграл')
                    break
                elif value_sum == 21:
                    print(f'Банкир победил {value_sum}')
                    break
                print(f'Сумма очков: {value_sum}\n')
            elif player_input == 'n':
                break
        return print(f'Итоговая сумма очков: {value_sum}')


# player = Player("Mike")
# player.get_result(player.get_card(), player.bets())
dealer = Dealer('Bob')
dealer.get_result(dealer.get_card(), dealer.bets())



# Банкир в свою очередь не может остановится на 15(петля)и обязан остановиться на 17(казна)

# Минимальная ставка 5$
# раздаётся по одной карте каждому игроку. Нужно набрать 21 очко, но не больше, либо больше, чем у твоего противника
# два туза - золотое очко. (при переборе туз идёт за одно очко по договорённости)
# банкир ставит максимальную ставку, всё, что у него есть
# раздаётся по одной карте банкиру и игроку, потом игрок делает ставку. Ставка не должна превышать суммы банка,
# потом просит карту, если количество очков достаточное (либо игрок набрал 21), то карты вскрываются, если игрок набрал 21,
# то автоматически выигрывает(в этом случае карты банкира не играют)
# Если у игрока достаточное количество очков и он вскрывается, то банкир вскрывает свою карту и набирает карты, до достаточного по его мнению
# количества. Если у банкира 16 очков, или менее, он обязан взять еще одну карту, если у банкира 17 очков, он не имеет права больше набирать карты
# При выигрыше игрок забирает свою ставку + сумму равную ставке из банка
# При проигрыше, ставка игрока идёт в банк
# При переборе игра останавливается
# Игра может продолжаться до того момента, пока не закончится банк, либо до того момента, пока не наступит
# "Стук" - это тот случай, когда в банке будет денег в три раза больше, чем было изначально
# https://www.youtube.com/watch?v=YxYx0eVeBK0 ссылка на правила игры
# максимальное количество карт, которые можно набрать =5
# Если у игрока выпало 21 и он взял ещё одну карту, то игрок проигрывает и платит штраф 10$
# Банкир при первой раздаче по одной карте, свою карту не показывает, когда игрок сказал хватит,
# то банкир открывает свою карту и набирает карты в открытую
# Игра вслепую с шестёркой реализовать



# def get_result(self, value, bet):
#     card_sum = 1
#     value_sum = value
#     while card_sum != 5:
#         player_input = input(f'Нужно дабавить карту {self.name} y/n?: ')
#         if player_input == 'y':
#             card_sum += 1
#             value_sum += Dealer.get_card(self)
#             if value_sum == 17:
#                 break
#             if value_sum > 21:
#                 print('Перебор, вы проиграли')
#                 break
#             print(f'Сумма очков: {value_sum}\n')
#         if player_input == 'n':
#             break
#     return print(f'Итоговая сумма очков: {value_sum}')