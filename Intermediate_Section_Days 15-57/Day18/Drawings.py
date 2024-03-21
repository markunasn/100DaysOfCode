import turtle
import random
cursor = turtle.Turtle()
turtle.colormode(255)

colors = ['AliceBlue', 'aquamarine', 'blue', 'brown',]

def drawShape(num_sides, obj):
    for i in range(num_sides):
        angle = 360 / num_sides
        obj.forward(100)
        obj.right(angle)

def gen_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    rgb = (red, blue, green)
    return rgb
def randomWalk(num, obj):
    for i in range(num):
        obj.pencolor(gen_color())
        obj.forward(25)
        obj.right(90*random.randint(1, 5))

#drawShape(3, cursor)

randomWalk(10,cursor)