from tkinter import *
from turtle import Screen, Turtle
import random

# width 800
# height 600

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600,width=800)
screen.title('Brick-Game')
screen.tracer(0)

paddle = Turtle()
paddle.shape('sqaure')
paddle.color('grey')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)


screen.listen()
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')

game_on = True
while game_on:
    screen.update()


difficulty_level = input('what is your leve of difficulty? Easy, Normal or Hard: ')

players = input('How many players will be playing? ')

color_choice = input('What is the color of your board Red or Blue? ')

def go_left():
    new_y paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_right():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


def power_up():
# a thingie will come if player takes it, they get a special power, life, larger, or something


def timer():
# how long a player has been playing

ss


def score():
# score for how many times they hit the brick



def level_up():
# when score reaches a level, they get a power




def lives():
# the lives a player has


def difficulty_level():
# hard, easy or normal



def color_board():
    # color of the board

def bonus_points():





def speed():
# hoq fast the ball comes


screen.exitonclick()
