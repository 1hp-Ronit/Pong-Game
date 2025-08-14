from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
CONTROLS1 = ('w', 's')
CONTROLS2 = ('Up', 'Down')
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

paddle = Turtle()
paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()
game_is_on = True


screen.listen()
screen.onkey(paddle_1.go_up, "w")
screen.onkey(paddle_1.go_down, "s")
screen.onkey(paddle_2.go_up, "Up")
screen.onkey(paddle_2.go_down, "Down")
while game_is_on:
    ball.move()
    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle_2
    if ball.distance(paddle_2) < 50 and ball.xcor() > 320 or ball.distance(paddle_1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
    screen.update()
screen.exitonclick()
