#Clase 3 "Ejemplos de Programas Secuenciales"

#Repaso de Algoritmo

#Algoritmo:Secuencia de pasos bien definida
#El algoritmo consta de una:
# Entrada ------ Algoritmo ------ Salida
# Entrada: input("mensaje a desplegar")
#Input siempre retorna un str y el usuario debe escribir el valor de input
# Salida: print("mensaje a desplegar")
#Print no retorna un valor osea imprime en la terminal el valor que escribe el usuario en input

# Problema 1

# Desarrolle un programa que solicite al usuario su nombre y luego el programa lo salude con su nombre

nombre = input("ingrese su nombre:")
print("buenos dias", nombre)
#la variable nombre tiene el valro de input para que el usuario responda a la pregunta planteada.
#Despues se imprime con el print para que salga en pantalla el mensaje y el nombre de la variable que se asigno y se le agrega una coma para que salga el mensaje y nombre

#Problema 2

#Desarrole un programa que solicite al usuario el ingreso de 2 numeros y luego muestre por pantalla de la suma de ambos 
edad1 = int(input("Ingresa tu edad:"))
edad2 = int(input("ingresa la edad de tu hermana:"))
suma = edad1 + edad2
print(suma) 
#Se utiliza int para que solo puedas entregar numeros ENTEROS y se logre a hacer la suma, con float numeros decimales, str (o sin nada) pega el texto junto

#Problema 3

#Escriba un programa que reciba la temperatura en grados Celsius y la convierta a grados Fahrenheit. La fórmula para la conversión es: F = C * 9/5 + 32
temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))
Celcius= (temperatura - 32) * 5/9
print("La temperatura en grados Celsius es:", Celcius)
#El float es para numeros decimales 

