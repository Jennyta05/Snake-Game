from turtle import Turtle
import random

class Food(Turtle):
   def __init__(self):
        super().__init__()
        self.shape("turtle")    
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5 )
        self.color("lightgreen")    
        self.speed("fastest")
        self.refresh()
               
   def refresh(self):  # aqui hacemos que la comida salga aleatoriamente
        random_x = random.randint(-200,200)
        random_y = random.randint(-200,200)
        self.goto(random_x, random_y)
        
        