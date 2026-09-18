#Nivel 10: El Movimiento del Jugador (Matrices + Modificación)Objetivo: Mover un personaje 'P' en un mapa vacío.Este es el ejercicio más difícil. Combina todo.Crea un mapa de 3x3 lleno de ceros 0.Coloca al jugador 'P' en la posición [0][0] (Fila 0, Columna 0).Imprime el mapa.Pregunta al usuario: "¿Mover Derecha o Abajo?".Dependiendo de la respuesta:Borra la 'P' de la posición actual (pon un 0).Cambia los índices (si es Derecha, suma 1 a la columna; si es Abajo, suma 1 a la fila).Coloca la 'P' en la nueva posición.Imprime el nuevo mapa.
import random
import os
yx = random.randint(7, 16)
terreno=[]
for y in range(yx):
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

j = "😎"
terreno[0][0] = j
pos_y = 0
pos_x = 0

for e in range(yx):
  print(terreno[e])

while True:
  os.system('cls' if os.name == 'nt' else 'clear')

  for e in range(yx):
    print(terreno[e])
  mov = input("a = izqierda, w = arriba, d = derecha, s = abajo    respuesta --->  ")
  

  if mov == "d":
    if pos_x < yx -1:
      if terreno[pos_y][pos_x +1] != "🧱":
        terreno[pos_y][pos_x] = "__"
        pos_x += 1
        terreno[pos_y][pos_x] = j
      else:
        print("No se puede cruzar por las paredes")
    else:
      print("No puedes cruzar, es el limite del mundo")
  elif mov == "s":  
    if pos_y < yx -1 :
      if terreno[pos_y +1][pos_x] != "🧱":
        terreno[pos_y][pos_x] = "__"
        pos_y += 1
        terreno[pos_y][pos_x] = j
      else:
        print("No se puede cruzar por las paredes")
    else:
      print("No puedes cruzar, es el limite del mundo")
  elif mov == "a":
    if pos_x > 0:
      if terreno[pos_y][pos_x -1] != "🧱":
        terreno[pos_y][pos_x] = "__"
        pos_x += -1
        terreno[pos_y][pos_x] = j
      else:
        print("No se puede cruzar por las paredes")
    else:
      print("No puedes cruzar, es el limite del mundo")
  elif mov == "w":
    if pos_y > 0:
      if terreno[pos_y -1][pos_x] != "🧱":
        terreno[pos_y][pos_x] = "__"
        pos_y += -1
        terreno[pos_y][pos_x] = j
      else:
        print("No se puede cruzar por las paredes")
    else:
      print("No puedes cruzar, es el limite del mundo")
  #for e in range(yx):
   # print(terreno[e])