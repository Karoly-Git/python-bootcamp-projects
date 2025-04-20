from turtle import Turtle

class Field(Turtle):
    def __init__(self, dim_x, dim_y):
        super().__init__()
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.DASH_NUM = 20

        # Draw the borders
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-self.dim_x / 2, -self.dim_y / 2)
        self.pendown()
        self.pensize(3)

        for _ in range(2):
            self.forward(dim_x)
            self.left(90)
            self.forward(dim_y)
            self.left(90)

        # Draw the middle dashed line
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -dim_y / 2)
        self.setheading(90)
        self.pensize(1)

        for _ in range(self.DASH_NUM):
            self.pendown()
            self.forward(dim_y / (2 * self.DASH_NUM))
            self.penup()
            self.forward(dim_y / (2 * (self.DASH_NUM - 1)))










