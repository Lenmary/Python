import os
resp=1
while resp !=0:
    print ("Paint (1)")
    print("Calculadora (2)")
    print("Iniciar sesión en instagram (edge) (3)")
    print("Iniciar sesión en facebook (edge) (4)")
    print("Salir(5)")
    resp=int(input("Elija una opción: "))
    if (resp == 1):
        os.system("mspaint")
    elif(resp==2):
        os.system("calc")
    elif(resp==3):
        os.system("Start microsoft-edge:https://www.instagram.com/")
    elif(resp==4):
        os.system("Start microsoft-edge:https://es-la.facebook.com/")
    elif(resp==5):
        print ("No entiendo esa orden") 