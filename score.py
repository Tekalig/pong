from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.__left_score = 0
        self.__right_score = 0
        self.goto(position)
        self.write(f"{self.__left_score}  {self.__right_score}", align="center", font=("monospace", 18, "bold"))

    def count(self, word):
        self.clear()
        if word == "l":
            self.__left_score += 1
        elif word == "r":
            self.__right_score += 1
        self.write(f"{self.__left_score}  {self.__right_score}", align="center", font=("monospace", 18, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=("Monospace", 24, "bold"))

    def winning_score(self):
        return max(self.__left_score, self.__right_score)
