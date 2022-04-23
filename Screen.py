import csv
from turtle import Turtle
from Game import game_over_turtle

score_printing_turtle = Turtle()
score_printing_turtle.ht()
score_printing_turtle.penup()
score_printing_turtle.pencolor('white')
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # ,(-60,0),(-80,0)]
home_screen_turtle = Turtle()
global difficulty
difficulty = 2
difficulty_turtle = Turtle()
difficulty_turtle.pencolor('white')
difficulty_turtle.penup()
difficulty_turtle.ht()
difficulty_options = ['', 'Easy', 'Medium', 'Hard']


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



def game_over(tim):
    tim.penup()
    tim.ht()
    tim.goto(0, 0)
    tim.pencolor('white')
    tim.write("Game over.", font=('OCR A Extended', 24, 'normal'), align='center')
    tim.goto(0, -30)
    tim.write("Press enter to play again", font=('OCR A Extended', 16, 'normal'), align='center')
    tim.goto(0, -60)
    tim.write("Press escape to return to homescreen", font=('OCR A Extended', 16, 'normal'), align='center')


def easy():
    global difficulty
    difficulty = 1
    from main import screen
    screen.tracer(0)
    difficulty_turtle.clear()
    difficulty_turtle.write(f"Current Difficulty-   {difficulty_options[difficulty]}",
                            font=('OCR A Extended', 16, 'normal'), align='center')
    screen.update()


def medium():
    global difficulty
    difficulty = 2
    from main import screen
    screen.tracer(0)
    difficulty_turtle.clear()
    difficulty_turtle.write(f"Current Difficulty-   {difficulty_options[difficulty]}",
                            font=('OCR A Extended', 16, 'normal'), align='center')
    screen.update()


def hard():
    global difficulty
    difficulty = 3
    from main import screen
    screen.tracer(0)
    difficulty_turtle.clear()
    difficulty_turtle.write(f"Current Difficulty-   {difficulty_options[difficulty]}",
                            font=('OCR A Extended', 16, 'normal'), align='center')
    screen.update()


def home_screen():
    from main import screen
    home_screen_turtle.penup()
    home_screen_turtle.ht()
    home_screen_turtle.pencolor('white')
    home_screen_turtle.goto(0, 200)
    home_screen_turtle.write("Select difficulty by pressing 1, 2, or 3", font=('OCR A Extended', 16, 'normal'), align='center')
    screen.onkeypress(easy, '1')
    screen.onkeypress(medium, '2')
    screen.onkeypress(hard, '3')
    screen.onkeypress(score_menu, 'Tab')
    difficulty_turtle.goto((0, 100))
    difficulty_turtle.write(f"Current Difficulty-   {difficulty_options[difficulty]}",
                            font=('OCR A Extended', 16, 'normal'), align='center')
    home_screen_turtle.goto(0, 0)
    home_screen_turtle.write("Press Enter to begin", font=('OCR A Extended', 16, 'normal'), align='center')
    home_screen_turtle.goto(0, -100)
    home_screen_turtle.write("Press Tab to view scores", font=('OCR A Extended', 16, 'normal'), align='center')
    home_screen_turtle.goto(0, -320)
    home_screen_turtle.write("Instructions to play- \nUse arrow keys to turn the snake.\nThe snake grows on eating food which appear as blue coloured dots.\nThe game ends if the snake's head touches its body.", font=('OCR A Extended', 14, 'normal'), align='center')


def return_to_homescreen():
    from Game import snake_is_alive
    from Game import game_on
    from main import screen, turtle_for_main_heading, turtle_for_displaying_messages
    snake_is_alive = False
    screen.tracer(0)
    screen.onkeypress(game_on,'Return')
    game_over_turtle.clear()
    home_screen_turtle.clear()
    difficulty_turtle.clear()
    score_printing_turtle.clear()
    screen.update()
    home_screen()


def score_menu():
    from main import screen
    screen.onkeypress('None','Return')
    from main import screen
    import csv
    screen.tracer(0)
    game_over_turtle.clear()
    home_screen_turtle.clear()
    difficulty_turtle.clear()
    score_printing_turtle.clear()
    score_printing_turtle.goto(150, -315)
    score_printing_turtle.write('Press right arrow key to sort by high score', font=('OCR A Extended', 13, 'normal'),
                                align='center')

    score_printing_turtle.goto(0, 200)
    data_file = open('Scores.csv')
    rdr = csv.reader(data_file)
    i = 0
    scores = []
    for row in rdr:
        if row != []:
            scores.append(row)
    for row in scores:

        text = row[0] + '\t' + '\t' + row[1]
        if i == 0:

            score_printing_turtle.write(text, font=('OCR A Extended', 24, 'normal'), align='center')
            score_printing_turtle.goto(score_printing_turtle.xcor(), score_printing_turtle.ycor() - 30)
            i = 1
        else:
            score_printing_turtle.write(text, font=('OCR A Extended', 16, 'normal'), align='center')
            score_printing_turtle.goto(score_printing_turtle.xcor(), score_printing_turtle.ycor() - 30)

    screen.update()
    screen.onkeypress(highscore, 'Right')


def highscore():
    import csv
    from main import screen
    screen.onkeypress('None', 'Return')
    screen.tracer(0)
    score_printing_turtle.clear()
    game_over_turtle.clear()
    home_screen_turtle.clear()
    difficulty_turtle.clear()
    score_printing_turtle.goto(150, -315)
    score_printing_turtle.write('Press left arrow key to see recent scores', font=('OCR A Extended', 13, 'normal'),
                                align='center')

    score_printing_turtle.goto(0, 200)
    data_file = open('Scores.csv')
    rdr = csv.reader(data_file)
    i = 0
    scores = []
    for row in rdr:
        if row != []:
            scores.append(row)

    scores.sort(reverse=True)
    for row in scores:
        text = row[0] + '\t' + '\t' + row[1]
        if i == 0:

            score_printing_turtle.write(text, font=('OCR A Extended', 24, 'normal'), align='center')
            score_printing_turtle.goto(score_printing_turtle.xcor(), score_printing_turtle.ycor() - 30)
            i = 1
        else:
            score_printing_turtle.write(text, font=('OCR A Extended', 16, 'normal'), align='center')
            score_printing_turtle.goto(score_printing_turtle.xcor(), score_printing_turtle.ycor() - 30)

    screen.update()
    screen.onkeypress(score_menu, 'Left')
