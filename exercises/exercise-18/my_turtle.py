from turtle import Turtle, Screen
import random
import math

screen = Screen()
screen.colormode(255)  # Allow RGB values from 0 to 255

t = Turtle()

def random_color():
    """
    Generate a random RGB color.

    Returns:
        tuple: A tuple of three integers representing an RGB color,
               where each value is between 0 and 255.
    """
    return tuple(random.randint(0, 255) for _ in range(3))


def draw_polygons(max_side_count=10, side_length=100):
    """
    Draw a series of polygons starting from a triangle up to a specified maximum side count.

    Args:
        max_side_count (int): The maximum number of sides for the largest polygon.
        side_length (int): The length of each side of the polygons.

    The turtle will draw each polygon in a random color, increasing the side count by one each time.
    """
    t.showturtle()
    t.shape("turtle")
    t.pensize(1)

    for n in range(3, max_side_count + 1):
        t.color(random_color())
        for _ in range(n):
            t.forward(side_length)
            t.right(360 / n)

def random_walk(step_num=100, step_length=20):
    """
    Perform a random walk using the turtle graphics module.

    Args:
        step_num (int): Number of steps the turtle will take.
        step_length (int): Distance the turtle moves forward each step.

    The turtle changes to a random color and a random cardinal direction
    (0, 90, 180, or 270 degrees) on each step, creating a colorful path.
    """
    t.hideturtle()
    t.speed('fastest')
    t.pensize(10)

    for _ in range(step_num):
        t.color(random_color())
        t.forward(step_length)
        t.setheading(random.choice([0, 90, 180, 270]))

def draw_spirograph(radius=100, gap=5):
    """
    Draws a colorful spirograph pattern using the turtle graphics module.

    Parameters:
    radius (int): The radius of each individual circle that makes up the spirograph. Default is 100.
    gap (int): The angle in degrees to rotate after drawing each circle. Smaller values create more detailed patterns. Default is 5.

    Each circle is drawn in a randomly chosen color, and the turtle rotates by 'gap' degrees before drawing the next.
    """
    t.speed(0)  # Max speed for smooth drawing
    for deg in range(0, 360, gap):
        t.left(gap)
        t.color(random_color())
        t.circle(radius)

# draw_polygons()
# random_walk()

draw_spirograph()

screen.exitonclick()
