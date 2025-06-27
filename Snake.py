from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.snake_creator(position)
    def move(self):
        for seg_num in range(len(self.segments) - 1 ,0, -1):  # 0 is stop point
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)  # Move the first added

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def increase_snake_size(self):

        self.snake_creator(self.segments[len(STARTING_POSITIONS)-1].position())


    def snake_creator(self,position):
        snake = Turtle("square")
        snake.color("green")
        snake.penup()
        snake.shapesize(0.8,0.8)
        snake.goto(position)
        self.segments.append(snake)
    def detect_collision(self):
        get_x = self.head.xcor()
        get_y = self.head.ycor()

        for segment in self.segments[1:]: # Don't care about head, we can handle this using slicing
            if self.head.distance(segment) < 15:
                return True

        if get_x >= 300 or get_x <= -300 or get_y >= 300 or get_y <= -300:
            return True
        else:
            return False