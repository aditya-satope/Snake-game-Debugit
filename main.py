from turtle import Turtle, Screen
from Game import game_on

from Screen import *
import keyboard
screen = Screen()
screen.setup(width=900, height=800)

screen.bgcolor('black')
screen.title('Snake game!!!!')
home_screen()


screen.listen()

print('hi')
print('foiasjdfopj')
screen.onkeypress(game_on, 'Return')


screen.exitonclick()
