#tipos de datos y variables: integer (int), float, string (str)
#it convierte letras en string en números
#float sirve para leer decimales
edad = 0
estatura = 0.0
peso = 0
nombre = "" 
#input lee información 
nombre = input("Hola, como te llamas?")
edad = int (input("Cuantos años tiene?"))
estatura=float(input("Cuál es su estatura?"))
peso = float(input("Cuál es su peso en kg?"))
imc = peso/(estatura*estatura) 
#**2 al cuadrado 
print ("Su imc es:", imc)
#== comparacion de igualdad, != desigualdad


if(edad >= 18 and edad <= 70):
    print ("Eres mayor de edad")
#elif = else if
elif (edad < 18 and edad >=11):
    print ("Eres menor de edad")
else:
    print ("Datos no válidos")