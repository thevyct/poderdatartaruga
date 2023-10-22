#Desafio: Variáveis e loops
#Hegágono

lados = 6
angulo = 3660 / lados

from turtle import *

speed(4)
shape("turtle")

for count in range(lados):
    forward(100)
    right(60)

done()