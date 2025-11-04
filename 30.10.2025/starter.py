from PZ2 import *
import random
Circle = lambda x: 3.14*x**2
Square = lambda y: y**2
filtr = lambda z:  z>=20
spi = []
for i in range(5):
    a =random.randint(1, 10)
    spi.append(a)

SumAreaCircle=list(map(Circle, spi))
SumAreaSquare=list(map(Square, spi))
print(SumAreaCircle)
print(SumAreaSquare)
FilterSumAreaCircle=list(filter(filtr, SumAreaCircle))
FilterSumAreaSquare=list(filter(filtr, SumAreaSquare))
print(FilterSumAreaCircle)
print(FilterSumAreaSquare)
    

    
