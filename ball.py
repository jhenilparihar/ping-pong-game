from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(315)
        self.move_speed = 0.1

    def move(self):
        self.goto((self.xcor()+self.x), (self.ycor()+self.y))

    def bounce_wall(self):
        self.y *= -1

    def bounce_paddle(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.x *= -1
        self.move_speed = 0.1
