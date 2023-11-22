from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.color_choice = 0
        self.goto(-100, 200)
        self.write(self.color_choice, align='center', font=('Courier', 80, normal))


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.color_choice, align='center', font=('Courier', 80, 'normal'))


    def point_up(self):
        self.color_choice += 1
