import random

num_ran = random.randint(0, 100)
rept = 'intentalo de nuevo: '
num_adiv ='¿Estoy pensando un numero del 0 al 100, cual es? '

def numero_val(num):
    while True:
        try:
            num_adiv = int(input(num))
            return num_adiv
        except ValueError:
            print(f'el simbolo no es un numero, {rept}')

numero = numero_val(num_adiv)

while True:

    if 100 >= numero >= 0:
        if numero < num_ran:
            print(f'Tu numero esta abajo de el numero que estoy pensando.')
            numero = numero_val(rept)
            continue
        elif numero > num_ran:
            print(f'Tu numero esta arriba del numero que estoy pensando.')
            numero = numero_val(rept)
            continue
        else:
            print('Felicidades acabas de atinarle al numero')
            break
    else:
        print('ese numero no esta en mi base de datos...')
        numero = numero_val(rept)
        continue
