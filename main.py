

from turtle import Turtle, Screen
import time   #sirve para manejar el tiempo
import turtle 
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
#creacion del tablero del juego

screen = Screen()  #los parenesis indican que queremos que se cree un objeto
screen.setup(width=600, height= 600) #aqui indicamos el tamaño del fondo
screen.bgpic("space.png") #aqui le ponemos color al fondo
screen.title("snake game") # aqui le decimos el titulo de arriba

screen.tracer(0)  #anulamos la animacion automatica



        #contruir cuerpo serpiente

""" #crear una lista que almacena una tuplas (coordenadas)
starting_position = [(0,0),(-20,0),(-40,0)]

#almaceno los segmentos de la serpiente
segments = [] #almacenamos los snake segment

 """
#animacion serpiente
game_is_on = True  

 #crear/instanciar a la serpiente
snake = Snake()
#crear/instanciar a la comida
food = Food()
#crear/instanciar tablero 
scoreboard = ScoreBoard()


#metodo escucha de las teclas
screen.listen() #esta pendiene de recibir instrucciones
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update() #se acualiza la pagina
    time.sleep(0.1) #mas pequeño el numero mas rapido la animacion
 
    snake.move()

    """ for segment in segments:
        segment.forward(20) 
        #segment.left(90)
 """
    if snake.head.distance(food) < 15:   #condicional para que coma
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #condicion para detecar paredes
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()

        #detector de colisiones de segmento de serpiente
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False  
            scoreboard.game_over()  
   
    
    


screen.exitonclick() #salir al darle click

"""
snake_segment = Turtle("square") #se instancio (se convirtio en objeto) a un cuadrado
snake_segment.color("white") ya creamos un cuadrado blanco

snake_segment2 = Turtle("square") 
snake_segment2.color("pink")
snake_segment2.goto(-20, 0)  (primero x y va de 20 en 20)ayuda a ubicar un turtle en un plano cartesiano

snake_segment3 = Turtle("square") 
snake_segment3.color("pink")
snake_segment3.goto(-40, 0) 
"""






