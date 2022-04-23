def nouse():
    pass


from turtle import Turtle

game_over_turtle = Turtle()

snake_is_alive=True
def game_on():
    from turtle import Turtle
    import time
    from main import screen
    from snake import Snake
    import food
    from scoreboard import Scoreboard,update_score_to_file
    from Screen import create_screen, game_over, home_screen_turtle, difficulty, difficulty_turtle, return_to_homescreen
    import random, datetime
    screen.onkeypress(None, 'Escape')
    screen.onkeypress(None, '1')
    screen.onkeypress(None, '2')
    screen.onkeypress(None, '3')
    screen.onkeypress(None, 'Return')
    screen.onkeypress(None,'Tab')
    datetime_object = datetime.datetime.now()
    date_and_time=str(datetime_object)[0:19]
    print(date_and_time)
    game_over_turtle.clear()
    home_screen_turtle.clear()
    difficulty_turtle.clear()
    game_is_on = True
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
    print(difficulty)
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

    while True:
        if game_is_on:
            screen.update()
            snake.move_snake()
            if difficulty == 1:
                time.sleep(0.2)
            elif difficulty == 2:
                time.sleep(0.1)
            elif difficulty == 3:
                time.sleep(0.05)

            screen.onkeypress(snake.up,'Up')
            screen.onkeypress(snake.right, 'Right')
            screen.onkeypress(snake.left, 'Left')
            screen.onkeypress(snake.down, 'Down')
            snake.out_of_boundary()
            if not snake_is_alive:
                for segment in snake.segments:
                    segment.ht()
                break
            if snake.detect_collision():
                game_over(game_over_turtle)
                update_score_to_file(date_and_time,score)
                screen.onkeypress(game_on, 'Return')
                screen.onkeypress(return_to_homescreen, 'Escape')
                snake_food.ht()
                scoreboard.clear()
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
