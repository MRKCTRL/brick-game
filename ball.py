from tutrle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
    # paddle = Turtle()
    self.shape('circle')
    self.color('white')
    self.penup()
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.goto(positon)


        def move(self):
            new_y self.ycor() + 10
            new_x self.xcor() + 10
            self.goto(new_y, new_x)
