from tkinter import CENTER, font
from turtle import Turtle, update

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.goto(0,260)
        self.color("purple")
        self.update_score()
        self.hideturtle() #ocultamos la tortuga

    def update_score(self):
        self.write(f"Puntaje :{self.score}", font=("Arial",24,"bold"), align="center") #la f es para que funcione concatenar variables

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.write("GAME OVER >:D", font=("Arial",24,"bold"), align="center")
        

