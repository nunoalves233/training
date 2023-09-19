import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
import turtle
ninja = turtle.Turtle()
ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.roght(30)

    ninja.penup()
    ninja.position(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()    