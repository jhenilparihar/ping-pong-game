from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 200)
        self.write(f"{self.paddle1_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(50, 200)
        self.write(f"{self.paddle2_score}", move=False, align=ALIGNMENT, font=FONT)
