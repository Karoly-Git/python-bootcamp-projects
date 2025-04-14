from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)  # Allow RGB values from 0 to 255

t = Turtle()
t.shape("turtle")

# n = 3
# while n < 10:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     t.color(r, g, b)
#     
#     for _ in range(n):
#         t.forward(100)
#         t.right(360 / n)
#     
#     n += 1

t.hideturtle()
t.speed('fastest')
t.pensize(10)
n = 0
step_num = 500
while n < step_num:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    t.color(color)
    t.forward(20)
    t.setheading(random.choice([0, 90, 180, 270]))

    n += 1

# t.showturtle()
screen.exitonclick()
