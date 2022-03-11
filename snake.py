from turtle import Turtle



STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

#constructor
    def __init__(self):  #def es lo mismo que function
        #almaceno los segmentos de la serpiente
        self.segments = [] #con self le decimos que es un atributo de la clase
        #metodo que crea la serpiente
        self.create_snake()
        #atributo cabeza
        self.head = self.segments[0]

    def create_snake(self):
       for position in STARTING_POSITION:
           self.add_segment(position) 

#guardo los segment
    def add_segment(self, position):
         snake_segment = Turtle("square") 
         snake_segment.color("#FA8072")
         snake_segment.penup()  
         snake_segment.goto(position) 
         self.segments.append(snake_segment) 

    def extend(self):
        self.add_segment(self.segments[-1].position())    

    def move(self):
      for seg_num in range(len(self.segments)-1,0,-1): #creamos un rango y el len nos conviere en int los objetos
        
        new_x = self.segments[seg_num-1].xcor()
        new_y = self.segments[seg_num-1].ycor()
        self.segments[seg_num].goto(new_x,new_y)
      self.head.forward(20)
   
    def up(self):
      if self.head.heading() != DOWN:  #condicionamos para que no se devuelva
          self.head.setheading(UP) #los grados hacia donde se mueve/ en este caso arriba

    def down(self):
      if self.head.heading() != UP:
          self.head.setheading(DOWN)

    def left(self):
      if self.head.heading() != RIGHT:
          self.head.setheading(LEFT)

    def right(self):
      if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)