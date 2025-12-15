import time
from time import *
from Animal import Animal
from Food import Food

class Times:


    def __init__(self, time_eat, animal, food):
        self.time_eat = time_eat
        self.animal = animal
        self.food = food

    def set_eat(self, time_eat, animal, food):
        self.time_eat = time_eat
        self.animal = animal
        self.food = food

    def time_up(self):
        disk = []
        i = 0
        try:
            Times.time_up(disk[i], disk[i + 1], disk[i + 2])
            if self.time_eat == time.localtime():
                print(f"{self.animal} говорит ом ом ом {self.food} как вкустно ")
            i = i + 3
        except:
            i = 0
            self.times.sleep(1)


