from turtle import Turtle
from main import screen
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0),(-60,0),(-80,0),(-100,0),(-120,0)]


class Snake:
    def __init__(self):
        self.color = 'green'
        self.segments = []
        self.create_snake()

    def create_snake(self):

        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        # self.segments[0].shape('triangle')

    def move_snake(self):

        for i in range(len(self.segments) - 1, 0, -1):
            new_location_xcor = self.segments[i - 1].xcor()
            new_location_ycor = self.segments[i - 1].ycor()
            self.segments[i].goto(new_location_xcor, new_location_ycor)
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        screen.onkeypress(None, 'Up')
        screen.onkeypress(None, 'Right')
        screen.onkeypress(None, 'Left')
        screen.onkeypress(None, 'Down')
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
        else:
            pass

    def left(self):
        screen.onkeypress(None, 'Up')
        screen.onkeypress(None, 'Right')
        screen.onkeypress(None, 'Left')
        screen.onkeypress(None, 'Down')
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
        else:
            pass

    def right(self):
        screen.onkeypress(None, 'Up')
        screen.onkeypress(None, 'Right')
        screen.onkeypress(None, 'Left')
        screen.onkeypress(None, 'Down')
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
        else:
            pass

    def down(self):
        screen.onkeypress(None, 'Up')
        screen.onkeypress(None, 'Right')
        screen.onkeypress(None, 'Left')
        screen.onkeypress(None, 'Down')
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
        else:
            pass

    def increase_length(self):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        position = self.segments[-1].pos()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def head_position(self):
        return self.segments[0].pos()

    def tail_position(self):
        return self.segments[-1].pos()

    def all_segment_coordinates(self):
        all_pos = []
        for segment in self.segments:
            all_pos.append(segment.pos())
        return all_pos

    def all_segment_coordinates_except_head(self):
        all_pos = []
        for segment in self.segments:
            all_pos.append(segment.pos())
        return all_pos[1::]

    def detect_collision(self):
        segments_without_head = self.segments[1::]
        for segment in segments_without_head:
            if self.segments[0].distance(segment) < 10:
                return True
                break
        else:
            return False

    def out_of_boundary(self):
        if self.head_position()[0] > 375:
            self.segments[0].goto(-375, self.head_position()[1])
        elif self.head_position()[1] > 320:
            self.segments[0].goto(self.head_position()[0], -320)
        elif self.head_position()[0] < -375:
            self.segments[0].goto(375, self.head_position()[1])
        elif self.head_position()[1] < -320:
            self.segments[0].goto(self.head_position()[0], 320)

