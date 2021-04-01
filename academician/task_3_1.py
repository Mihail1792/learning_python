### **Какая пора года??**
# Ваша задача — реализовать функцию `get_season(date)`, которая принимает объект `Date` и возвращает соответствующую ему пору года.
# Пора года должна быть типа `string`.
# В английском поры года имеют следующие наименования: весна — spring, лето — summer, осень — autumn (fall), зима — winter.
# Если аргумент `date` не был передан, функция должна выбросить исключение `'Unable to determine the time of year!'`
# Если аргумент `date` **некорректный**, функция должна выбросить исключение (`Error`).
# Напишите свой код в `.{your_name}/what_season.py`.


class Date:
    def __init__(self,day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


    def get_season(self):
        if self.month == 12 or self.month == 1 or self.month == 2:
            return "Winter"
        elif self.month == 3 or self.month == 4 or self.month == 5:
            return "Spring"
        elif self.month == 6 or self.month == 7 or self.month == 8:
            return "Summer"
        else:
            return "Autumn"

a = Date(19, 9, 2017)
print(a.get_season())
