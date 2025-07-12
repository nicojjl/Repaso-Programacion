#Problema 1

#Desarrole un programa que solicite el ingreso del radio de un circulo y muestre por pantalla el area y perimetro de la circunferencia. 
Radio = float(input("Ingrese el radio del circulo: "))
Area = 3.14 * Radio ** 2
Perimetro = 2 * 3.14 * Radio
print("El area del circulo es:", Area , "cm^2", "y el perimetro es:", Perimetro , "cm")
#Para aproximar el perimetro o el Area podemos utilizar round (area, a) siendo a el numero de decimales que quieres aproximar.

#Problema 2

#En el sistema imperial de medidas, un pie tiene doce pulgadas. Una pulgada es igual a 2.54 centímetros. Escriba un programa que reciba la estatura de una persona en pies y pulgadas, y la entregue en centimetros, siguiendo el formato del ejemplo:
Pies = int(input("Ingrese la estatura en pies: "))
pulgada = int(input("Ingrese la estatura en pulgadas: "))
Estatura = Pies * 2.54 * 12 + pulgada * 2.54
print ("Tu estatura en centimetros es:", Estatura, "cm")