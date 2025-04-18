from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_forwards():
    """Move the turtle forward by 10 units."""
    t.forward(10)

def move_backwards():
    """Move the turtle backward by 10 units."""
    t.backward(10)

def turn_clockwise():
    """Rotate the turtle 5 degrees clockwise."""
    t.right(5)

def turn_counter_clockwise():
    """Rotate the turtle 5 degrees counterclockwise."""
    t.left(5)

def clear_screen():
    """Clear all drawings from the screen without closing the window."""
    t.reset()

s.listen()

s.onkey(move_forwards, "w")
s.onkey(move_backwards, "s")
s.onkey(turn_clockwise, "a")
s.onkey(turn_counter_clockwise, "d")
s.onkey(clear_screen, "c")

s.exitonclick()
