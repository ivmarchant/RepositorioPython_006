#Crear ciclo for que permita ingresar 10 numeros. Mostrar cuantos sin numeros pares y cuantos son impares

par = 0
impar = 0
for i in range(10):
    num = int(input("Digite un numero: "))
    if (num%2 == 0):
        par = par + 1
    else:
        impar = impar + 1
print("La cantidad de numeros pares es: " + str(par))
print("La cantidad de numeros impares es: "+ str(impar))