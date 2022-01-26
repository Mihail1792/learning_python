class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError ('Слабый пароль')

    def save(self):
        with open('users', 'a') as r:
            r.write(f'{self.login, self.password}'+'\n')


class V2(Verification):

    def __init__(self, login, password):
        Verification.__init__(self, login, password)
        self.save()

    def save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}'+'\n' == i:
                    raise ValueError('Пользователь с такими данными уже существует')
        Verification.save(self)

    def show(self):
        return self.login, self.password




x = V2('LOL31', '12345ss67s85')

print(x.show())
