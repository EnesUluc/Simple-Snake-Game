from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("config/ScoreDataBase.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.color("yellow") # If you don't change the color before you write , anything change
        self.update_score_board()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("config/ScoreDataBase.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()
    def update_score_board(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score:{self.high_score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_score_board()
