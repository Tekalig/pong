from turtle import Turtle


class Slider(Turtle):
    def __init__(self, position, color):
        super().__init__(shape="square")
        self.color(color)
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

        # screen bisector
        bi = Turtle(shape="square", visible=False)
        bi.color('white')
        bi.penup()
        bi.goto(0, -350)
        bi.left(90)
        for i in range(40):
            bi.pendown()
            bi.forward(20)

    def up(self):
        if self.ycor() < 260:
            y = self.ycor()+20
            self.goto(self.xcor(), y)

    def down(self):
        if self.ycor() > -260:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)

