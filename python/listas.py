calificaciones = [1,2,3,4,5]
nombres=["Móises", "Camila", "Fernanda", "Pablo", "Tania"]
lista_variadas= [True, 10.5, "abc", [0,1,1]]

print ("estudiante: ", nombres[3])
print ("calificación: ", calificaciones[3])
print ("Lista dentro de otra ", lista_variadas[3][0])
print("imprimir un rango o slices ", nombres[1:3])
print (lista_variadas)

#agregar elementos a listas
nombres.append("Annibal")
print (nombres)

#remover
nombres.remove("Pablo")
print (nombres)

nombres.append("Lola")
print (nombres)

print  (nombres[0:5])
