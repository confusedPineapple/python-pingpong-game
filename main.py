from turtle import Screen
from turtle import Turtle
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time
import winsound

screen = Screen()
screen.setup(width=1100, height= 600)
screen.bgcolor('black')
screen.title('My PingPong Game <3')
screen.tracer(0)
r_paddle = Paddle((500, 0))
l_paddle = Paddle((-500, 0))
ball = Ball()
scoreboard = Scoreboard()

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 80


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect Collision with r_paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 340 or ball.distance(l_paddle) < 30 and ball.xcor() < -340 :
        # winsound.Beep(frequency, duration)
        ball.bounce_x()


    # Detect out of bounds ball
    #Right
    if ball.xcor() > 600:
        scoreboard.l_point()
        ball.goto(0,0)
        ball.x_move = -10
        ball.y_move = -10
        ball.move_speed = 0.1
        ball.move()

    #Left
    elif ball.xcor() < -600 :
        scoreboard.r_point()
        ball.goto(0,0)
        ball.x_move = 10
        ball.y_move = 10
        ball.move_speed = 0.1
        ball.move()





screen.exitonclick()