from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Fish(Animal):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def eat(self):
        return f"Рыба {self.name} ({self.species}) питается планктоном и водорослями."
    def move(self):
        return f"Рыба {self.name} плавает, изгибая тело и используя плавники."
    def __str__(self):
        return f"Рыба: {self.name}, Вид: {self.species}"


class Bird(Animal):
    def __init__(self, name, species, can_fly=True):
        self.name = name
        self.species = species
        self.can_fly = can_fly

    def eat(self):
        if "хищн" in self.species.lower():
            return f"Птица {self.name} ({self.species}) охотится на мелких животных."
        else:
            return f"Птица {self.name} ({self.species}) питается семенами и насекомыми."
    def move(self):
        if self.can_fly:
            return f"Птица {self.name} летает, махая крыльями."
        else:
            return f"Птица {self.name} ходит по земле или плавает (нелетающая птица)."
    def __str__(self):
        return f"Птица: {self.name}, Вид: {self.species}"
