from turtle import *
import random

colors = ['red', 'black', 'blue', 'green']
color(colors[random.randint(0, 3)], colors[random.randint(0, 3)])
begin_fill()
counter = 0;
while counter < 3:
    forward(100)
    left(20)
    counter += 1
end_fill()
done()