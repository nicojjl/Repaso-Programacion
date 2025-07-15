#Condiciones Logicas

#Simbolos de operadores logicos y su interpretacion

# > Mayor que
# < Menor que
# >= Mayor o igual que
# <= Menor o igual que
# == Igual que
# != Diferente que

#Ejemplo: "ire en bicicleta a comprar si no esta lloviendo y si el negocio esta a menos de 5km"
# clima != lluvia Y distancia < 5km
# sea Y == and

#Ejemplo 2: "Haces deporte si es martes o jueves"
# dia == martes O dia == jueves
# sea O == or

#Ejemplo 3: "Haces deporte si es martes o jueves y  hay sol"
# (dia == martes and clima == sol) or (dia == jueves and clima == sol)
# clima == sol and (dia== artes or dia == jueves)
# Es estilo P^(Q or R) y q o r deben ser verdaderos para que se cumpla la condicion