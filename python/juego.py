import random  
while True:
    aleatorio= random.randrange(0,3)
    eligePc= ""
    print ("Piedra (1)")
    print ("Papel (2)")
    print ("Tijera (3)")
    opcion= int(input("Elija una opción"))

    if opcion == 1:
        eligeUsuario = "Piedra"
    elif opcion == 2:
        eligeUsuario ="Papel"
    elif opcion== 3:
        eligeUsuario = "Tijera"
    print("Elegiste: ", eligeUsuario)

    if aleatorio == 0:
        eligePc= "Piedra"
    elif aleatorio ==1:
        eligePc= "Papel"
    elif aleatorio == 2:
        eligePc ="Tijera"
    print ("La máquina eligió: ",eligePc)
    print ("...")

    if eligePc == "Piedra" and eligeUsuario == "Papel":
        print ("Ganaste, papel envuelve a piedra")
    elif eligePc == "Papel" and eligeUsuario == "Tijera":
        print ("Ganaste, tijera corta papel")
    elif eligePc == "Tijera" and eligeUsuario == "Piedra":
        print("Ganaste, piedra machaca tijera")
    elif eligePc=="Papel" and eligeUsuario == "Piedra":
        print ("Perdiste, papel envuelve piedra")
    elif eligePc == "Tijera" and eligeUsuario == "Papel":
        print("Perdiste, tijera corta papel")
    elif eligePc == "Tijera" and eligeUsuario == "Piedra":
        print ("Perdiste, piedra machaca tijera")
    elif eligePc == eligeUsuario:
        print("Emmmmpate")