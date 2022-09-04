from turtle import Turtle
import random
UP=90
DOWN=270

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-350, 0)
        self.color("red")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.point=0
    def down(self):
            self.point-=20
            self.goto(-350,self.point)
    def up(self):
            self.point+=20
            self.goto(-350,self.point)



class RightPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(350, 0)
        self.color("blue")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.point=0
    def down(self):
            self.point-=20
            if self.ycor()>-220:
                self.goto(350,self.point)
    def up(self):
            self.point+=20
            if self.ycor() < 220:
                self.goto(350,self.point)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("slowest")
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("black")
        self.shape("circle")
        self.xmove=10
        self.ymove=10
        self.movespeed=0.1
    def move(self):
        newx=self.xcor()+self.xmove
        newy=self.ycor()+self.ymove
        self.goto(newx,newy)
    def bounce_y(self):
        self.ymove=self.ymove*(-1)

    def bounce_x(self):
        self.xmove=self.xmove*(-1)
        self.movespeed =self.movespeed*0.9

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
    def setboard(self,pos):
        self.goto(pos, 250)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    def increascore(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))




