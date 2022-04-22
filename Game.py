def nouse():
    pass
from turtle import Turtle
game_over_turtle = Turtle()

def game_on():
    from turtle import Turtle
    import time
    from main import screen
    from snake import Snake
    import food
    from scoreboard import Scoreboard
    from Screen import create_screen, game_over, home_screen_turtle
    import random

    game_over_turtle.clear()
    home_screen_turtle.clear()
    game_is_on = True
    print(game_is_on, 'inside the loop')
    scoreboard = Scoreboard()
    score = 0
    scoreboard.write_score()
    time.sleep(0.5)
    snake = Snake()
    screen.listen()
    snake_food = food.Food()
    new_food_x = random.randint(-280, 280)
    new_food_y = random.randint(-280, 280)
    snake_food.goto(new_food_x, new_food_y)
    game_is_on = True
    print(id(game_is_on))

    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

    while True:
        if game_is_on:
            screen.update()
            snake.move_snake()
            time.sleep(0.1)
            screen.onkeypress(snake.up,
                              'Up')  # Don't write function parenthesis inside this function just the function name
            screen.onkeypress(snake.right, 'Right')
            screen.onkeypress(snake.left, 'Left')
            screen.onkeypress(snake.down, 'Down')
            screen.onkeypress(nouse, 'Return')
            snake.out_of_boundary()
            if snake.detect_collision():

                game_over(game_over_turtle)
                screen.onkeypress(game_on, 'Return')
                snake_food.ht()
                for segment in snake.segments:
                    segment.ht()
                break
            if 15 > snake.head_position()[0] - snake_food.pos()[0] > -15:
                if 15 > snake.head_position()[1] - snake_food.pos()[1] > -15:
                    Segments = snake.segments
                    snake_food.generate_food(Segments)
                    snake.increase_length()
                    score += 1
            scoreboard.update_score(score)
        else:
            snake = False
