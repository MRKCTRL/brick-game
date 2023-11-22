from tutrle import Turtle

class Paddle(Turtle):


    def __init__(self, position):
        super().__init__()
    # paddle = Turtle()
    self.shape('sqaure')
    self.color('grey')
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.goto(positon)


    def go_left(self):
        new_y self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_right(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
