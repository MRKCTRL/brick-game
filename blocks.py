from tutrle import Turtle

class Block(Turtle):


    def __init__(self, position):
        super().__init__()
    # paddle = Turtle()
    self.shape('rectangle')
    self.color('green')
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.goto(positon)


    def row(self):
        new_y self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def row(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
