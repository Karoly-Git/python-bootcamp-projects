from turtle import Turtle, Screen
import random
import tkinter.messagebox

screen = Screen()
screen.setup(width=500, height=400)

# Draw the start line
start_line = Turtle()
start_line.hideturtle()
start_line.penup()
start_line.goto(-230, -150)
start_line.left(90)
start_line.pendown()
start_line.forward(300)

# Label the start line
start_label = Turtle()
start_label.hideturtle()
start_label.penup()
start_label.goto(-200, 160)
start_label.write("START", align="center", font=("Arial", 14, "bold"))

# Draw the finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(230, -150)
finish_line.left(90)
finish_line.pendown()
finish_line.forward(300)

# Label the finish line
finish_label = Turtle()
finish_label.hideturtle()
finish_label.penup()
finish_label.goto(200, 160)
finish_label.write("GOAL", align="center", font=("Arial", 14, "bold"))

is_race_on = False

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "blue", "green", "gold", "orange", "purple"]

while user_bet not in colors:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt=f"Which turtle will win the race? Choose from: {', '.join(colors)}"
    )
    if user_bet:
        user_bet = user_bet.lower()

all_turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                tkinter.messagebox.showinfo("Race Result", f"You've won! The {winning_color} turtle is the winner!")
            else:
                tkinter.messagebox.showinfo("Race Result", f"You've lost! The {winning_color} turtle won the race.")

screen.exitonclick()
