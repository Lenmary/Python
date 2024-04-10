intentos = 0
usuarios_autenticados = {"admin":"123", "len":"456","pepe":"9090"}
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña ")

if ( usuario in usuarios_autenticados):
    while intentos <= 3:
        if (usuarios_autenticados[usuario] == password):
            print("ACESSO CORRECTO")
            break
        else:
            print("ACCESO DENEGADO")
            intentos+=1
            password = input(f"Contraseña incorrecta, intento {intentos} de 3. Reescriba la contraseña: ")
            
else:
     print("El usuario no existe")