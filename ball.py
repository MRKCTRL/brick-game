from tutrle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
    # paddle = Turtle()
    self.shape('circle')
    self.color('white')
    self.penup()
    self.x_move = 10
    self.y_move = 10



        def move(self):
            new_y self.ycor() + self.y_move
            new_x self.xcor() + self.x_move
            self.goto(new_y, new_x)


        def bounc(self):
            self.y_move *= -1
