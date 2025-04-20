import tkinter as tk
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from field import Field
import time

FIELD_DIM_X = 600
FIELD_DIM_Y = 400
PADDLE_L_COLOR = "yellow"
PADDLE_R_COLOR = "blue"
PADDLE_DIM_X = 20
PADDLE_DIM_Y = 100
GAP = 10  # Distance between the paddle and the border
BALL_SIZE = 20

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")

# Maximize the window (Windows-friendly)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.state('zoomed')  # For Windows. On Mac/Linux, try: root.attributes('-zoomed', True)

screen.tracer(0)

field = Field(FIELD_DIM_X, FIELD_DIM_Y)
paddle_L = Paddle(PADDLE_DIM_X, PADDLE_DIM_Y, GAP, PADDLE_L_COLOR, FIELD_DIM_X, FIELD_DIM_Y, side=-1)  # Left paddle
paddle_R = Paddle(PADDLE_DIM_X, PADDLE_DIM_Y, GAP, PADDLE_R_COLOR, FIELD_DIM_X, FIELD_DIM_Y, side=+1)  # Right paddle
ball = Ball(shape="circle", color="white", size=BALL_SIZE)

screen.update()

game_is_on = True

# Keybindings
screen.listen()

screen.onkey(paddle_L.up, "w")
screen.onkey(paddle_L.down, "s")
screen.onkey(paddle_R.up, "Up")
screen.onkey(paddle_R.down, "Down")

def new_round():
    global game_is_on
    if not game_is_on:
        ball.reset()
        paddle_L.reset()
        paddle_R.reset()
        screen.update()
    game_is_on = True

screen.onkey(new_round, "n")

# Game
def play_game():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.017)  # ~60 FPS

        ball.move()

        # Bounce off the top and bottom walls
        if ball.ycor() > (FIELD_DIM_Y / 2 - BALL_SIZE / 2) or ball.ycor() < -(FIELD_DIM_Y / 2 - BALL_SIZE / 2):
            ball.bounce_y()

        # Detect collision with paddles using range check
        xcor_limit = FIELD_DIM_X / 2 - GAP - PADDLE_DIM_X - BALL_SIZE / 2

        if abs(ball.xcor() + xcor_limit) < 5 and paddle_L.ycor() - PADDLE_DIM_Y / 2 <= ball.ycor() <= paddle_L.ycor() + PADDLE_DIM_Y / 2:
            ball.bounce_x()

        if abs(ball.xcor() - xcor_limit) < 5 and paddle_R.ycor() - PADDLE_DIM_Y / 2 <= ball.ycor() <= paddle_R.ycor() + PADDLE_DIM_Y / 2:
            ball.bounce_x()

        # Detect ball out of bounds based on full field dimensions
        if ball.xcor() < -FIELD_DIM_X / 2 or ball.xcor() > FIELD_DIM_X / 2:
            game_is_on = False

screen.onkey(play_game, "Return")  # Bind Enter key to start the ball

screen.exitonclick()
