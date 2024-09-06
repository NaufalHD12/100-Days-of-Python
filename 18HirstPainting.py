import turtle
from turtle import Turtle, Screen
from random import choice
# turtle.colormode(255)

color_list = [(230, 227, 225), (229, 223, 226), (217, 227, 220), (195, 172, 121), (222, 227, 232), (157, 97, 59), (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85), (118, 162, 175), (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82), (207, 202, 146), (144, 176, 161), (178, 150, 156), (176, 202, 188), (217, 179, 172), (22, 77, 93), (33, 79, 62), (95, 143, 150), (160, 111, 117), (214, 178, 183), (168, 202, 212)]


def random_color():
    color = choice(color_list)
    return color


# initialize screen and turtle
screen = Screen()
screen.colormode(255)
t = Turtle()
t.speed("fastest")
t.penup()

# Set the first position
t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots = 100

for dot in range(1, num_of_dots + 1):
    t.dot(20,random_color())
    t.forward(50)

    if dot % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


t.hideturtle()
screen.exitonclick()
