from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.reset_position()
        self.resetting = False

    def move(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def reset_position(self):
        self.resetting = True
        self.hideturtle()
        self.speed("fastest")
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()
        self.resetting = False

    def finished(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

