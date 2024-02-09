from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__();
        self.score = 0
        with open("highscores.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    """
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    """

    def restart(self):

        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscores.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
