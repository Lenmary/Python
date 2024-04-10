notas = []
suma = 0

for x in range(3):
    nota = int(input("Ingrese la nota: "))
    notas.append(nota)
    suma = suma + nota

promedio = suma/3
print("El promedio es: ", promedio)
if promedio > 1.7:
    print("Aprobado")
else:
    print("Reprobado, guee gue gue") 