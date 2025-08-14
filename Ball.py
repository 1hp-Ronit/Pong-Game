from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#f1be4d")
        self.shape("circle")
        self.penup()
    def move(self):
        time.sleep(0.1)
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
