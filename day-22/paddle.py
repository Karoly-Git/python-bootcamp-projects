from turtle import Turtle

class Paddle(Turtle):
    STEP_LENGTH = 20

    def __init__(self, dim_x, dim_y, gap, color, field_dim_x, field_dim_y, side):
        super().__init__()
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.gap = gap
        self.field_dim_x = field_dim_x
        self.field_dim_y = field_dim_y
        self.side = side
        
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=self.dim_y / 20, stretch_len=self.dim_x / 20)
        self.penup()
        # Start the paddle on the appropriate side (left or right)
        self.goto(self.side * ((self.field_dim_x - self.dim_x) / 2 - self.gap), 0)

    def up(self):
        """Move the paddle up if within field bounds."""
        if self.ycor() < (self.field_dim_y / 2 - self.dim_y / 2):
            self.goto(self.xcor(), self.ycor() + self.STEP_LENGTH)

    def down(self):
        """Move the paddle down if within field bounds."""
        if self.ycor() > -(self.field_dim_y / 2 - self.dim_y / 2):
            self.goto(self.xcor(), self.ycor() - self.STEP_LENGTH)

    def reset(self):
        """Reset the paddle to its starting position."""
        self.goto(self.side * ((self.field_dim_x - self.dim_x) / 2 - self.gap), 0)
