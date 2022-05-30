from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_dot()
        self.refresh()

    def create_dot(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        x_coord = random.randint(-280, 280)
        y_coord = random.randint(-280, 280)
        self.goto(x_coord, y_coord)

    def refresh(self):
        x_coord = random.randint(-280, 280)
        y_coord = random.randint(-280, 280)
        self.goto(x_coord, y_coord)
