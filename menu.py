#Crear menu con 3 opciones
import os

def Numeros():
    #Ingresar n numeros, donde n es un numero ingresado por teclado
    #Mostrar: Cantidad de números positivos, camtidad de negativos, cantidad de números iguales
    #a cero
    pos = 0
    neg = 0
    igu = 0
    a = int(input("Digite la cantidad de números a ingresar: "))
    for i in range(a):
        num = int(input("Numero " + str(i) +": " ))
        if(num > 0):
            pos = pos + 1
        if (num < 0):
            neg = neg + 1
        else:
            igu = + 1
    print("La cantidad de N° positivos es: " + str(pos))
    print("La cantidad de N° negativos es: " + str(neg))
    print("La cantidad de N° iguales a 0 es: " + str(igu))
    pausa = input("Apriete enter para terminar...")

def Personas():
    #ingresar para n personas: nombre y edad. Mostrar promedio de todas las edades ingresadas.
    sumita =  0
    conta = 0

    b = int(input("Digite la cantidad de personas: "))
    for i in range(b):
        nom = input("Ingrese Nombre: ")
        ed = int(input("Ingrese edad: "))
        conta+=1
        sumita+=ed
    
    print("Promedio de las edades: " + str(sumita/ conta))
    pausa = input("Presione enter...")

seguir = True
while (seguir):
    os.system('cls')
    print("1. Numeros.")
    print("2. Datos Personales")
    print("3. Salir.")
    op = int(input("Digite opción 1, 2, 3: "))
    if (op == 1):
        Numeros()           #Involamos metodo
    if (op == 2):
        Personas()
    if (op == 3):
        print("Programa Finalizado")
        pausa = input("Apriete enter para terminar...")
        break