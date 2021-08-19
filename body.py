from turtle import Turtle


class GameBody(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.create_game()

    def create_game(self):
        self.pencolor("white")
        self.pensize(3)
        self.right(90)
        for i in range(59):
            if i % 2 == 0:
                self.penup()
                self.forward(10)
            else:
                self.pendown()
                self.forward(10)
