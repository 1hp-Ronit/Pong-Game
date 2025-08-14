from turtle import Turtle, Screen


class Paddle(Turtle, Screen):
    def __init__(self, cor):
        super().__init__()
        self.coordinates = cor
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(cor)
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


