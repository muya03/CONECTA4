#MOHAMED ALHOWAIDI CONECTA CUATRO

from turtle import Screen, Turtle
from random import randint 

print("__MOHAMED ALHOWADI NASRALLA CONECTA CUATRO__")

Primer_jugador = input(("Nombre del primer jugador "))
Segundo_jugador = input(("Nombre del segundo jugador "))

while Primer_jugador == Segundo_jugador:
    print("Por favor cambie el nombre del Segundo jugador")
    Segundo_jugador = input(("Nombre del segundo jugador "))


alto = 600
ancho = 700
radio= (alto/14)

def partida():
    tablero = construye_tablero()
    pantalla = prepara_pantalla()
    tort = prepara_tortuga()
    dibuja_tablero(tort)
    turno = randint(1,2)
    if turno == 1:
        turno = Primer_jugador
    else:
        turno = Segundo_jugador
    
    

    ganador = None
    while ganador == None:
        [fila, columna] = lee_jugada(tablero, turno)
        #print([fila, columna])
        
        dibuja_jugada(tort, turno, fila, columna)
        if turno == Primer_jugador:
            turno = Segundo_jugador
        else:
            turno = Primer_jugador
        escribir_turno(turno, tort)
        ganador = busca_ganador(tablero, fila, columna)

    if ganador == "empate":
        print("")
        print("EMPATE")
        print("")

    else:
        print("")
        print("Ha ganado " + ganador)
        print("")


def prepara_tortuga():

    tort = Turtle()
    tort.speed(0)
    tort.hideturtle()
    tort.pensize(2)
    return tort

def prepara_pantalla():

    pant = Screen()
    pant.setup(ancho + 50, alto + 50)
    pant.screensize(ancho, alto)
    pant.setworldcoordinates(0,0,ancho,alto)
    pant.bgcolor()
    return pant

def construye_tablero():

    Matriz=[]


    for i in range(6):
        Matriz.append([" "] * 7)
        

    return Matriz

def dibuja_tablero(tort):
    n = 5
    m=radio + n
    

    tort.fillcolor("#1B75C0")
    tort.begin_fill()
    for i in range(2):
        
        tort.forward(ancho)
        tort.left(90)
        tort.forward(alto)
        tort.left(90)
    tort.end_fill()

    for i in range (7):

        for j in range(6):
            tort.penup()
            tort.setheading(0)
            tort.goto(2*radio*i + m,2*radio*j + n)
            tort.setheading(90)
            tort.forward(15*j)
            tort.setheading(0)
            tort.forward(15*i)         
            tort.pendown()
            tort.pensize(1)   
            tort.setheading(0)
            tort.fillcolor("white")
            tort.begin_fill()
            tort.circle(radio)
            tort.end_fill()

            if i<0:
                
                m = radio 
                

def lee_jugada(tablero, turno):

      print("El turno es de " + turno)
      columna = int(input("Columna => ")) -1

      while columna < 0 or columna > 6:
          columna = int(input("Numero no aceptado, inserte un numero de nuevo. Columna => ")) -1

      for i in range(6):
          if tablero[i][columna] == " ":
              fila = i

      while tablero[fila - 0][columna] != " ":
          columna = int(input("Numero no aceptado, inserte un numero de nuevo. Columna => ")) -1
         
      tablero[fila][columna] = turno
      return [fila,columna]

def dibuja_jugada(tort, turno, fila, columna):

    tort.pensize(1)
    x = (2*radio*columna)+radio+15*columna+5
    y = (radio*(6-fila))+15*(5-fila)+radio*(5-fila)+5

    if turno == Primer_jugador:

          for i in range(6):

              if i < fila-i:
              
            
                  tort.penup()
                  tort.goto(x,(radio*(6-i))+15*(5-i)+radio*(5-i)+5)
                  tort.setheading(270)
                  tort.forward(radio)
                  tort.pendown()
                  tort.setheading(0)
                  tort.fillcolor("red")
                  tort.begin_fill()
                  tort.circle(radio)
                  tort.end_fill()
                  tort.fillcolor("white")
                  tort.begin_fill()
                  tort.circle(radio)
                  tort.end_fill()

              if i == 5:
                  
                  tort.penup()
                  tort.goto(x,y)
                  tort.setheading(270)
                  tort.forward(radio)
                  tort.pendown()
                  tort.setheading(0)
                  tort.fillcolor("red")
                  tort.begin_fill()
                  tort.circle(radio)
                  tort.end_fill()


    if turno == Segundo_jugador:

        for i in range(6):

              if i < fila-i:
              
            
                  tort.penup()
                  tort.goto(x,(radio*(6-i))+15*(5-i)+radio*(5-i)+5)
                  tort.setheading(270)
                  tort.forward(radio)
                  tort.pendown()
                  tort.setheading(0)
                  tort.fillcolor("green")
                  tort.begin_fill()
                  tort.circle(radio)
                  tort.end_fill()
                  tort.fillcolor("white")
                  tort.begin_fill()
                  tort.circle(radio)
                  tort.end_fill()


              if i == 5:
                  
                  tort.penup()
                  tort.goto(x,y)
                  tort.setheading(270)
                  tort.forward(radio)
                  tort.pendown()
                  tort.setheading(0)
                  tort.fillcolor("green")
                  tort.begin_fill()
                  tort.circle(radio)
                  tort.end_fill()

                  
             
def busca_ganador(tablero, fila, columna):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            gana = gana_fila(fila, columna, tablero)
            if gana != None:
                return gana

    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            gana = gana_columna(fila, columna, tablero)
            if gana != None:
                return gana

    for columna in range(4):
        for fila in range(3):
 
            gana = gana_diagonal_derecha(tablero, fila, columna)
            if gana != None:
                return gana

    
    for columna in range(4):
        for fila in range(3,6):
            gana = gana_diagonal_izquierda(tablero, fila, columna)
            if gana != None:
                return gana

    if empate(tablero, fila, columna):
        return "empate"
    return None
      
def gana_fila(fila, columna, tablero):

    if(columna + 3 < len(tablero[0]) and
    tablero[fila][columna] == tablero[fila][columna+1] == tablero[fila][columna+2] == tablero[fila][columna+3] != " "):

        return tablero[fila][columna] 


def gana_columna(fila, columna, tablero):

    if(fila + 3 < len(tablero) and
    tablero[fila][columna] == tablero[fila+1][columna] == tablero[fila+2][columna] == tablero[fila+3][columna] != " "):

        return tablero[fila][columna]

def gana_diagonal_derecha(tablero, fila, columna):
    

    if tablero[fila][columna] != " " and tablero[fila+1][columna+1] == tablero[fila][columna] and tablero[fila+2][columna+2] == tablero[fila][columna] and tablero[fila+3][columna+3] == tablero[fila][columna]:

        return tablero[fila][columna]



def gana_diagonal_izquierda(tablero, fila, columna):

    if tablero[fila][columna] != " " and tablero[fila-1][columna+1] == tablero[fila][columna] and tablero[fila-2][columna+2] == tablero[fila][columna] and tablero[fila-3][columna+3] == tablero[fila][columna]:
                

        return tablero[fila][columna]


def empate(tablero, fila, columna):

    for fila in range(6):
        for columna in range(7):
            
            if tablero[fila][columna]== " ":
                return False
    return True

def escribir_turno(turno, tort):

    tort.penup()
    tort.goto(0, - 25)
    tort.write("El turno es de " + turno, font=("Verdana", 
                                    15, "normal")) 
    



 
partida()
















        
