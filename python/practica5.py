traductor = {"amor":"love", "abrazo":"hug", "arbol":"tree"}
palabra = ""
while palabra != "0":
    palabra = input("Ingrese la palabra a traducir: ")
    if palabra in traductor:
        print("Traduciendo...")
        print(f"(esp): {palabra} (eng): {traductor[palabra]}")
    elif (palabra !="0"):
        print("No se encuentra la palabra. Desea añadir al diccionario?")
        resp = input("(S/N) ")
        if resp == "S":
            traductor[palabra]= input("Ingrese la palabra a traducir ")
            print("Se ha añadido correctamente")
            print(traductor)
        else:
            print("Cerrando diccionario...")
    elif(resp=="0"):
        print("Cerrando diccionario...")
        
