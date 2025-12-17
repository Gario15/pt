import math
from abc import ABC, abstractmethod
#Вариант2
#Задание1
class Polygon:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

#Задание2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

#Задание3
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Fish(Animal):
    def eat(self):
        return "Рыба ест планктон"

    def move(self):
        return "Рыба плавает в воде"


class Bird(Animal):
    def eat(self):
        return "Птица ест зерно"

    def move(self):
        return "Птица летает в небе"

#Задание4
class Student:
    def __init__(self, last_name):
        self.last_name = last_name
        self.grades = []

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            print("Ошибка: оценка должна быть числом")
            return
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)