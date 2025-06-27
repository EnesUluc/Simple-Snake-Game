from turtle import Screen
import ScoreBoard
import time
import Snake
import Food

# BIRAZ DUZENLE OZELLIKLE DOSYA OKUMA YAZMA KISIMLARINI
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(600, 600)

# Create the screen

screen.tracer(0)

snake = Snake.Snake() #moduleName.className()
food = Food.Food() # Create a food from food class
score_board = ScoreBoard.ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_is_on = True


sleep_count = 0.08
while game_is_on:
    screen.update()
    time.sleep(sleep_count)
    snake.move()
    if snake.detect_collision():
        game_is_on = False
        score_board.reset()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase_snake_size()

        score_board.increase_score()
        sleep_count -= 0.002

screen.exitonclick()