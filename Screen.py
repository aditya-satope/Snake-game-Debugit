import time
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # ,(-60,0),(-80,0)]
home_screen_turtle=Turtle()


def create_screen(tim):
    tim.speed(8)
    tim.color('white')
    tim.ht()
    tim.penup()
    x = 385
    y = 330
    tim.goto(-1 * x, y)
    tim.pendown()
    tim.goto(375, y)
    tim.goto(375, -1 * y)
    tim.goto(-1 * x, -1 * y)
    tim.goto(-1 * x, y)
    tim.penup()
    tim.goto(0,330)
    tim.write("The Snake Game", font=('Arial', 30, 'normal'), align='center')
def game_over(tim):
    from main import game_is_on
    tim.penup()
    tim.ht()
    tim.goto(0,0)
    tim.pencolor('white')
    tim.write("Game over.", font=('Arial', 24, 'normal'), align='center')
    tim.goto(0,-30)
    tim.write("Press enter to play again", font=('Arial', 16, 'normal'), align='center')

def home_screen():
    home_screen_turtle.penup()
    home_screen_turtle.ht()
    home_screen_turtle.pencolor('white')
    home_screen_turtle.goto(0,30)
    home_screen_turtle.write("Press enter to begin", font=('Arial', 16, 'normal'), align='center')