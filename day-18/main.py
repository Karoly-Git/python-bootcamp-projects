import colorgram
from turtle import Turtle, Screen
import random

# Setup screen and turtle
screen = Screen()
screen.colormode(255)
t = Turtle()
t.speed("fastest")
t.hideturtle()

# Extract colors from image
colors = colorgram.extract('img.png', 50)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

def draw_dot_line(num_dots, gap):
    """
    Draws a horizontal line of colored dots.

    Args:
        num_dots (int): Number of dots to draw in the line.
        gap (int): Space between each dot in pixels.
    """
    for _ in range(num_dots):
        t.dot(20, random.choice(rgb_colors))  # draw a colored dot
        t.forward(gap)

def build_paint(rows=10, columns=10, gap=50):
    """
    Builds a grid-like dot painting inspired by Damien Hirst's artwork.

    Args:
        rows (int): Number of rows in the painting.
        columns (int): Number of columns in the painting.
        gap (int): Distance between dots both horizontally and vertically.
    """
    t.penup()
    start_x = - (columns * gap) / 2
    start_y = - (rows * gap) / 2
    t.setpos(start_x, start_y)

    for row in range(rows):
        for col in range(columns):
            t.dot(20, random.choice(rgb_colors))
            t.forward(gap)
        # Move to the start of the next row
        t.setx(start_x)
        t.sety(start_y + gap * (row + 1))

build_paint(rows=10, columns=10, gap=50)

screen.exitonclick()
