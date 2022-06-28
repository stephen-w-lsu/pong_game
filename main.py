from turtle import Screen
import time
from ball import Ball
from court import Court
from paddle import Paddle
from paddle2 import Paddle2
from scoreboard import Scoreboard
from first_to_five import FirstToFive
from game_over import GameOver


screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

court_line = Court()
court_line.draw_dash()
court_line.draw_court()
scoreboard1 = Scoreboard(-300, 270)
scoreboard2 = Scoreboard(300, 270)
banner = FirstToFive()
banner.first_to_five()
paddle1 = Paddle()
paddle2 = Paddle2()
ball = Ball()
ball.random_start()
game_over = GameOver()

screen.listen()
screen.onkey(key="w", fun=paddle1.up)
screen.onkey(key="s", fun=paddle1.down)
screen.onkey(key="Up", fun=paddle2.up)
screen.onkey(key="Down", fun=paddle2.down)

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)

    ball.move()

    # Turn ball at paddle impact
    for seg in paddle1.seg_list:
        if seg.distance(ball.pos()) <= 15:
            if 90 < ball.heading() < 180:
                ball.up_even_turn()
            elif 180 < ball.heading() < 270:
                ball.down_turn()

    for seg in paddle2.seg_list:
        if seg.distance(ball.pos()) <= 15:
            if 0 < ball.heading() < 90:
                ball.up_even_turn()
            elif 270 < ball.heading() < 360:
                ball.down_turn()

    # Turn ball at top and bottom wall impact
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.top_bot_turn()

    # Stop paddles at boundaries
    if paddle1.head.ycor() >= 300:
        paddle1.down()
    elif paddle1.tail.ycor() <= -300:
        paddle1.up()

    if paddle2.head.ycor() >= 300:
        paddle2.down()
    elif paddle2.tail.ycor() <= -300:
        paddle2.up()

    # Increase score when ball passes left and right boundaries
    if ball.xcor() < -600:
        scoreboard2.increase_score()
        ball.random_start()

    if ball.xcor() > 600:
        scoreboard1.increase_score()
        ball.random_start()

    # Declares winner when one player scores 5
    if scoreboard1.score == 5 or scoreboard2.score == 5:
        game_over.game_over()
        if scoreboard1.score == 5:
            banner.player_1_win()
        elif scoreboard2.score == 5:
            banner.player_2_win()
        game_on = False

screen.exitonclick()
