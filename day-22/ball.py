from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, shape, color, size):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(0, 0)
        
        # Set ball speed based on size
        self.size = size
        self.reset_speed()

    def reset_speed(self):
        """Reset ball speed, randomize direction and magnitude based on size."""
        self.dx = random.choice([-2, 2]) * (self.size / 20)  # horizontal speed
        self.dy = random.choice([-2, 2]) * (self.size / 20)  # vertical speed

    def move(self):
        """Move the ball by the current speed."""
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce off the top or bottom walls."""
        self.dy *= -1

    def bounce_x(self):
        """Bounce off the left or right walls."""
        self.dx *= -1
        self.dx *= 1.05  # Slight speed increase
        self.dy *= 1.05  # Slight speed increase
        
        # Cap speed after a certain threshold to prevent runaway speed
        max_speed = 10  # Cap maximum speed to 10 units per frame
        if abs(self.dx) > max_speed:
            self.dx = max_speed * (self.dx / abs(self.dx))
        if abs(self.dy) > max_speed:
            self.dy = max_speed * (self.dy / abs(self.dy))

    def reset(self):
        """Reset the ball to the center and randomize speed/direction."""
        self.goto(0, 0)
        self.reset_speed()
