from ball import Ball
from turtle import Screen, Turtle
import random
from paddle import Paddle
import time
from block import Block

# width 800
# height 600

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600,width=800)
screen.title('Brick-Game')
screen.tracer(0)

red_paddle = Paddle((350,0))
blue_paddle = Paddle((350,0))
ball = Ball()
blocks = Block()


screen.listen()
screen.onkey(red_paddle, 'Left')
screen.onkey(red_paddle, 'Right')

screen.onkey(blue_paddle, 'w')
screen.onkey(blue_paddle, 's')

game_on = True
while game_on:
    time.sleep(0.2)
    screen.update()
    ball.move


# collison and dectecion
    if ball.ycor() -282:
        ball.bounce_y()


# hit on the paddle
    if ball.distance(red_paddle, blue_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    #  detect if it misses
    if ball.xcor() > -380:
        ball.reset_position()




difficulty_level = input('what is your leve of difficulty? Easy, Normal or Hard: ')

players = input('How many players will be playing? ')

color_choice = input('What is the color of your board Red or Blue? ')




screen.exitonclick()
