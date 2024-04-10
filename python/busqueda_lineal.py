import random 

def busqueda_lineal (lista, valor_buscado):
    existe = False

    for elemento in lista:
        if elemento == valor_buscado:
            existe = True
            break
    
    return existe

if __name__ == "__main__":
    tamaño_de_lista = int(input("Ingrese tamaño de la lista: "))
    valor_buscado = int(input("Ingrese el valor a ser buscado: "))
    lista =[]

    for i in range(tamaño_de_lista):
        lista.append(random.randint(0,tamaño_de_lista))

    existe_valor = busqueda_lineal(lista,valor_buscado)
    print(lista)
    print(f"El número {valor_buscado} {"existe" if existe_valor else "no está"} en la lista")