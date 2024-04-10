numero = 100000
while True:
    bandera = 0
    for x in range(2, numero):
        if(numero % x ==0):
            bandera= 1
            break

    if (bandera ==0):
        print(numero)

    bandera= 0
    numero+=1