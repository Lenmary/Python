edad = int(input("Ingrese su edad: "))

if (edad >=15 and edad <=18):
    print ("Licencia con permiso de padres")
elif (edad >=18 and edad < 65 ):
    print("licencia estandar")
elif (edad >= 65 and edad <75 ):
    print ("primero realizar un test")
else:
    print ("no autorizado")



numero_1 = int(input("ingrese el primer número: "))
numero_2= int(input("Ingrese el segundo número: "))

if(numero_1 > numero_2):
    print(f"{numero_1} es mayor a {numero_2}")
    if(numero_1 % 2 ==0):
        print("El número es par")
    else:
        print("El número es impar")
elif(numero_1 < numero_2):
    print(f"{numero_2}es mayor a {numero_1}")
    if(numero_2 % 2 == 0):
        print("el número es par")
    else:
        print("el número es impar")
else:
    print("los números ingresados son iguales")



print("........................................")

usuario = input("Ingrese su usuario: ")
password = int(input("Ingrese su contraseña: "))
if (usuario == "admin" and password == 123):
    print("Acceso correcto")
else:
    print("Acceso denegado")
