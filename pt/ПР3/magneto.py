class Rival:
    def __init__(self, initial_life=3):
        self.__life = initial_life

    def get_life(self):
        return self.__life

    def set_life(self, new_life):
        if new_life >= 0:
            self.__life = new_life
        else:
            print("Количество жизней не может быть отрицательным!")

    def attack(self):
        print("Ouch!")
        self.set_life(self.get_life() - 1)

    def checkLife(self):
        if self.get_life() <= 0:
            print("You won!")
        else:
            print(self.get_life())

thanos = Rival(3)  
magneto = Rival(5) 

print("Начало игры:")
thanos.checkLife()
magneto.checkLife()

print("Атакуем Таноса 3 раза:")
thanos.attack()
thanos.attack()
thanos.attack()

print("Результат после атак:")
thanos.checkLife()
magneto.checkLife()

print("Попытка установить Магнето -1 жизнь:")
magneto.set_life(-1)