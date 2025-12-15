#Зоопарк – управление животными и их кормлением.
from Times import Times
from Food import Food
from Animal import Animal
from pygame import display

#списки для хранения
AN = []
FO = []
while True:
    Times.time_up()
    a = input("доступные действия:\naddA - Добавляет животных\naddF - Добавляет рацирон")
    if a == "addA":
        AN.append(Animal())
    elif a == "addF":
        FO.append(Food())

#def __init__(main):
#    main.
