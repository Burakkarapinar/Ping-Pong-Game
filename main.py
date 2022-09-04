from turtle import  Screen
from createpaddle import Paddle, RightPaddle, Ball , Scoreboard
import time



screen = Screen()
screen.bgcolor("turquoise")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
gameison=True
paddle=Paddle()
paddleright=RightPaddle()
ball=Ball()
leftscore= Scoreboard()
leftscore.setboard(-250)
rightscore=Scoreboard()
rightscore.setboard(250)


screen.listen()
screen.onkey(paddle.up,"w")
screen.onkey(paddle.down,"s")
screen.onkey(paddleright.up,"Up")
screen.onkey(paddleright.down,"Down")

#ball.start()
while gameison:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    #detect up and top wall
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce_y()


    #detect wall
    if ball.xcor() > 400:
        time.sleep(1)
        ball.movespeed = 0.1
        ball.goto(0, 0)
        ball.bounce_x()
        leftscore.increascore()


    if ball.xcor() < -400:
        time.sleep(1)
        ball.movespeed=0.1
        ball.goto(0,0)
        ball.bounce_x()
        rightscore.increascore()


    #bounce from paddle
    if ball.distance(paddle)<50 and ball.xcor()<-338:
        ball.bounce_x()
    if ball.distance(paddleright)<50 and ball.xcor()>338:
        ball.bounce_x()









screen.exitonclick()
