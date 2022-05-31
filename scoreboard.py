from turtle import Turtle
ALIGNMENT = "center"
FONT= ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
