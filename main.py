# This is a pong script.
from turtle import Screen
from slider import Slider
from ball import Ball
from score import Score
import time
SLIDER_GAP = 40
WELL_GAP = 20

# create instance of a Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(0.8, 0.8)
screen.title("Pong Game")
screen.tracer(0)
width = screen.window_width()/2 - SLIDER_GAP
height = screen.window_height()/2 - WELL_GAP

# create instance of a slider and ball class and score
l_slider = Slider((-width, 0), "yellow")
r_slider = Slider((width, 0), "white")
ball = Ball()
score = Score((0, height-WELL_GAP))
# listen our key
screen.listen()
screen.onkey(r_slider.up, "Up")
screen.onkey(r_slider.down, "Down")
screen.onkey(l_slider.up, "w")
screen.onkey(l_slider.down, "s")

# game board
play_on = True
while play_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= height or ball.ycor() <= -height:
        ball.well_bounce()
    if (r_slider.distance(ball) < 50 or l_slider.distance(ball) < 50) and (ball.xcor() > width-WELL_GAP or ball.xcor() <-width+WELL_GAP):
        ball.slider_bounce()
    if ball.xcor() > width:
        score.count('l')
        ball.reset_position()
    if ball.xcor() < -width:
        score.count('r')
        ball.reset_position()
    if score.winning_score() == 5:
        play_on = False
        score.game_over()

screen.exitonclick()
