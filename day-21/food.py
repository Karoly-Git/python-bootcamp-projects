from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        grid_size = 20  # same as MOVE_DISTANCE
        random_x = random.randint(-14, 14) * grid_size
        random_y = random.randint(-14, 14) * grid_size
        self.goto(random_x, random_y)
