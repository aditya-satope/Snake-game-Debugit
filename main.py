from turtle import Turtle, Screen
from Game import game_on

from Screen import *
import keyboard
screen = Screen()
screen.setup(width=900, height=850)
screen.bgcolor('black')
screen.title('Snake game')


screen.tracer(0)
turtle_for_displaying_messages = Turtle()
turtle_for_main_heading=Turtle()
screen.addshape('lgog.gif')
turtle_for_main_heading.goto(0,370)
turtle_for_main_heading.shape('lgog.gif')
create_screen(turtle_for_displaying_messages)
screen.update()
home_screen()
screen.listen()
screen.onkeypress(game_on, 'Return')
screen.onkeypress(return_to_homescreen, 'Escape')
screen.onkeypress(score_menu,'Tab')
screen.mainloop()
