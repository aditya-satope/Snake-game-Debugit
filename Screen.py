import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # ,(-60,0),(-80,0)]
home_screen_turtle = Turtle()
global difficulty
difficulty = 2
difficulty_turtle = Turtle()
difficulty_turtle.pencolor('white')
difficulty_turtle.penup()
difficulty_turtle.ht()
difficulty_options=['','easy','medium','hard']

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
    tim.goto(0, 330)
    #tim.write("The Snake Game", font=('OCR A Extended', 30, 'normal'), align='center')


def game_over(tim):
    tim.penup()
    tim.ht()
    tim.goto(0, 0)
    tim.pencolor('white')
    tim.write("Game over.", font=('OCR A Extended', 24, 'normal'), align='center')
    tim.goto(0, -30)
    tim.write("Press enter to play again", font=('OCR A Extended', 16, 'normal'), align='center')


def easy():
    difficulty = 1
    from main import screen
    screen.tracer(0)
    difficulty_turtle.clear()
    difficulty_turtle.write(f"Current Difficulty {difficulty_options[difficulty]}", font=('OCR A Extended', 16, 'normal'), align='center')
    screen.update()


def medium():
    difficulty = 2
    from main import screen
    screen.tracer(0)
    difficulty_turtle.clear()
    difficulty_turtle.write(f"Current Difficulty {difficulty_options[difficulty]}", font=('OCR A Extended', 16, 'normal'), align='center')
    screen.update()


def hard():
    difficulty = 3
    from main import screen
    screen.tracer(0)
    difficulty_turtle.clear()
    difficulty_turtle.write(f"Current Difficulty {difficulty_options[difficulty]}", font=('OCR A Extended', 16, 'normal'), align='center')
    screen.update()


def home_screen():
    from main import screen
    home_screen_turtle.penup()
    home_screen_turtle.ht()
    home_screen_turtle.pencolor('white')
    home_screen_turtle.goto(0, 0)
    home_screen_turtle.write("Select difficulty between 1 to 3", font=('OCR A Extended', 16, 'normal'), align='center')
    home_screen_turtle.goto((0, -100))
    screen.onkeypress(easy, '1')
    screen.onkeypress(medium, '2')
    screen.onkeypress(hard, '3')
    difficulty_turtle.goto((0, -100))
    difficulty_turtle.write(f"Current Difficulty {difficulty_options[difficulty]}", font=('OCR A Extended', 16, 'normal'), align='center')
    home_screen_turtle.goto(0, -330)
    home_screen_turtle.write("Press enter to begin", font=('OCR A Extended', 16, 'normal'), align='center')
