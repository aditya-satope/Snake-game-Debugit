from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(0.5,0.5)
        self.penup()
    def generate_food(self,Segments):
        self.ht()   #to make turtle invisible
        self.color('blue')
        while True:
            new_food_x=random.randint(-280,280)
            new_food_y=random.randint(-280,280)
            for segment in Segments:
                if segment.distance(new_food_x,new_food_y) < 10:
                    break
            else:
                break
        self.goto(new_food_x,new_food_y)
        self.st()