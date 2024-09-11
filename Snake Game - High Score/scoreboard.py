from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        # Reading the High Score forom the file
        with open("Snake Game - High Score/data.txt") as file:
            self.high_score = int(file.read())

        self.score = 0

        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.color("white")

        self.update_scoreboard()

    
    def increaseScore(self):
        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font= FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Snake Game - High Score/data.txt","w") as file:
                file.write(f"{self.score}")
        
        self.score = 0
        
        self.update_scoreboard()
    

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font= FONT)
        
