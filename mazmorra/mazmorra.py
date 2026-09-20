#Nivel 10: El Movimiento del Jugador (Matrices + Modificación)Objetivo: Mover un personaje 'P' en un mapa vacío.Este es el ejercicio más difícil. Combina todo.Crea un mapa de 3x3 lleno de ceros 0.Coloca al jugador 'P' en la posición [0][0] (Fila 0, Columna 0).Imprime el mapa.Pregunta al usuario: "¿Mover Derecha o Abajo?".Dependiendo de la respuesta:Borra la 'P' de la posición actual (pon un 0).Cambia los índices (si es Derecha, suma 1 a la columna; si es Abajo, suma 1 a la fila).Coloca la 'P' en la nueva posición.Imprime el nuevo mapa.
import random
import os

def terreno():
  yx = random.randint(7, 16) #asigna un numero random entre 7 y 16
  terreno=[] # se crea el terreno(lista vacia)
  for y in range(yx): #empieza 
    lista = [] # de aqui voy agarrar la lista por partes para que se vea la matriz visualmente
    for x in range(yx):
      lista.append(random.randint(1,6))
      if lista[x] == 1 or lista[x] == 4:
        lista[x] = "🧱"

      if lista[x] == 2:
        lista[x] = "🧰"
      if lista[x] == 3 or lista[x] == 5 or lista[x] == 6:
        lista[x] = "__"
    terreno.append(lista)
  
  return terreno, yx

terr, yx = terreno()

j = "😎"
terr[0][0] = j
pos_y = 0
pos_x = 0

#for e in range(yx):
  #print(terr[e])

while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  for e in range(yx): #se imprime el terreno completo
    print(terr[e])

  mov = {'a':(0,-1), 'w':(-1,0), 'd':(0,1), 's':(1,0)}
  cont = input("a = izqierda, w = arriba, d = derecha, s = abajo    respuesta --->  ").lower()

  

  if cont in mov: 
    cordy, cordx = mov[cont]
    cord = {'s':yx-1 > pos_y, 'a':pos_x > 0, 'w':pos_y > 0,'d':yx-1 > pos_x}

 #pos_x < yx -1, pos_y < yx -1,  pos_x > 0, pos_y > 0     if pos_y < yx -1 :
    if cord[cont]:
      if terr[pos_y+cordy][pos_x+cordx] != "🧱":
        terr[pos_y][pos_x] = '__'
        pos_y += cordy
        pos_x += cordx
        terr[pos_y][pos_x] = j
      else:
        print("No se puede cruzar por las paredes")        
    else:
      print("No puedes cruzar, es el limite del mundo")

  