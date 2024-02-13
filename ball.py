from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('red')
        self.penup()
        self.__x_move = 10
        self.__y_move = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.__x_move
        y = self.ycor() + self.__y_move
        self.goto(x, y)

    def well_bounce(self):
        self.__y_move *= -1

    def slider_bounce(self):
        self.__x_move *= -1
        self.move_speed *= 0.65

    def reset_position(self):
        self.goto(0, 0)
        self.__x_move *= -1
        self.move_speed = 0.1