A demo solar system code using turtle in python 
import turtle
from math import *

screen=turtle.Screen()#creating the Screen
screen.tracer(50)

sun = turtle.Turtle()#turtle object for sun
sun.shape('circle')#shape of sun
sun.color('yellow')#color of sun

class Planet(turtle.Turtle):
    def __init__(self,name,radius, color):#initialize function
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    def move(self):
        x = self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle)

        self.goto(sun.xcor()+x,sun.ycor()+y)

        # making planets
mercury = Planet("Mercury",40, 'grey')
venus = Planet("Venus",80, 'orange')
earth=Planet("Earth",100,'blue')
mars = Planet("Mars",150, 'red')
jupiter=Planet("Jupiter",180, 'brown')
saturn=Planet("Saturn",230, 'pink')
uranus=Planet("Uranus",250, 'light blue')
neptune=Planet("Neptune",280, 'black')

#adding planets to a list
myList = [ mercury, venus,earth, mars,jupiter,saturn,uranus,neptune]


while True:#while statement
    screen.update()#updating the screen
    for i in myList:
        i.move()#moving the elements of the list

    # Increase the angle by 0.0x radians

    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005
