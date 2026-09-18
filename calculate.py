import math


print('Calculadora.\nUn proyecto para hacer calculos matematicos:')

def calculadora():

    def numero(pregunta):
        while True:
            try:
                num  = float(input(pregunta))
                return num
            except ValueError:
                print( 'debes colocar un numero.')
            

    def zero(num1, num2):           
        while True:
            try:
                return num1 / num2, num2
            except ZeroDivisionError:
                print('No se puede dividir los numero entre cero.')
            num2 = numero('Vuelve a colocar el segundo numero: ')

    def operacion():
        lista_op = ['/','+','*','**','-','÷','%','•','×','^']
        operador = input('Coloca el operador: ')
        while True:
            if operador in lista_op:
                return operador
            else:
                operador = input('No se permite esos simbolos en la operacion.\nIntenta colocar de nuevo el operador: ')

    num1 = numero('Coloca el primer numero: ')
    operador = operacion()
    num2 = numero('Coloca el segundo numero: ')




    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == "*" or operador == "×" or operador == '•':
        resultado = num1 * num2
    elif operador == '/' or operador == '÷':
        resultado, num2 = zero(num1, num2)
    elif operador == '**' or operador == '^':
        resultado = num1 ** num2
    elif operador == '%':
        resultado, num2 = zero(num1, num2)

    return num1, operador, num2, resultado


while True:
    num1, op, num2, res = calculadora()
    print(f'la operacion {num1} {op} {num2} es el resultado de {res}')
    seguir = input('¿Quieres hacer mas operaciones?.\n1.si\n2.no (cualquier otra letra o simbolo)\n \nRespuesta: ').lower()
    if seguir == 'si' or seguir == '1' or seguir == 'sí':
        continue
    else:
        break