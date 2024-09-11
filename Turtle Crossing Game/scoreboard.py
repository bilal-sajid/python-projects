from turtle import Turtle


FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
STARTING_POS = -220,260

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 1

        self.penup()
        self.goto(STARTING_POS)
        self.hideturtle()

        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)
    
    def level_up(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
    

