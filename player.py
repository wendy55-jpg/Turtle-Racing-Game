from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -250)
        self.setheading(90)

    def move_player(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(0, -250)

    def is_successful(self):
        if self.ycor() > 280:
            return True
        else:
            return False


