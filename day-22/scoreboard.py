from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self, field_dim_y):
        super().__init__()
        self.field_dim_y = field_dim_y  # <-- Store field_dim_y
        self.score_player_L = 0
        self.score_player_R = 0
        self.color("white")
        self.penup()
        self.goto(0, self.field_dim_y / 2 - 50)
        self.hideturtle()
        self.update_scores()

        # Create a separate Turtle for the message
        self.message_turtle = Turtle()
        self.message_turtle.color("white")
        self.message_turtle.penup()
        self.message_turtle.hideturtle()
        self.display_message('Press "Enter" to serve the ball.')

    def update_scores(self):
        self.clear()
        self.write(f"{self.score_player_L}   {self.score_player_R}", align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        if player == "L":
            self.score_player_L += 1
            self.display_message('Player L scores! Press "N" to start a new round.')
        elif player == "R":
            self.score_player_R += 1
            self.display_message('Player R scores! Press "N" to start a new round.')
        self.update_scores()

    def display_message(self, message):
        self.message_turtle.clear()  # Clear previous message if needed
        self.message_turtle.goto(0, self.field_dim_y / 2 + 20)  # 20px above field top
        self.message_turtle.write(message, align=ALIGNMENT, font=FONT)
