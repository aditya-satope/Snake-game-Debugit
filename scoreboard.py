from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.pencolor('white')
        self.write_score()

    def write_score(self):
        self.goto(0, 290)
        self.clear()
        self.write(f'Score = 0', align='center', font=("Arial", 16, "normal"))

    def update_score(self, score):
        self.clear()
        self.write(f'Score = {score}', align='center', font=("Arial", 16, "normal"))
