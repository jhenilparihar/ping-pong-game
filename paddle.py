from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(1, 5)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), (self.ycor()+30))

    def down(self):
        self.goto(self.xcor(), (self.ycor()-30))
